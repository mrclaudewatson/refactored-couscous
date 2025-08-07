#include "AVL_Database.hpp"
/*Sebastien Ghent U05939898 and Claude Watson U72087839 Project 3 AVL Tree Database*/

//Brief Overview Description of Code:

/*This program functions as a basic AVL tree database, designed for efficient record management and querying. 
The `Record` class encapsulates key-value pairs, while the `AVLNode` class represents tree nodes, maintaining pointers to left and right children and height information for balancing. 
The `AVLTree` class provides essential operations: `insertHelper` and `insert` for adding records, `deleteHelper` and `deleteNode` for removing records, and `searchHelper` and `search` for finding records. 
It ensures the tree remains balanced with rotations (`rotateRight` and `rotateLeft`) and rebalancing (`balanceNode`). 
The tree also supports `rangeQueryHelper` and `rangeQuery` for range queries, `inorderTraversalHelper` and `inorderTraversal` for sorted traversal, and `findKNearestHelper` and `findKNearestKeys` for nearest neighbor searches. 
Additionally, it includes functions to clear the tree (`clearHelper` and `clear`) and count records (`countRecordsHelper` and `countRecords`). 
The `IndexedDatabase` class integrates these AVL tree functions, providing a user-friendly interface for database operations, making the system an efficient and organized solution for record management.*/

Record::Record(const std::string& k, int v) : key(k), value(v) {} //Declaration of record constructor with key for the string and value
AVLNode::AVLNode(Record* r) : record(r), left(NULL), right(NULL), height(1) {} //Node Constructor which constructs a node that encapsulates the constructed record 
AVLTree::AVLTree() : root(NULL) {} //AVLTree Constructor to build the AVL tree
int AVLTree::height(AVLNode* node) { //AVLTree height function to retrieve the height of a node
    return node ? node->height : 0; // Return the node's height if the node exists, otherwise return 0
}
int AVLTree::balance(AVLNode* node) { //AVLTree balance node function
    return node ? height(node->left) - height(node->right) : 0;//If the node exists return the height of the left subtree from the right subtree otherwise return 0
}
int max(int a, int b) { //Return the Maximum of a and b
    return (a > b) ? a : b; //If a>b return a otherwise b
}
int abs(int a) { //Absolute value
    return (a < 0) ? -a : a; 
}
AVLNode* AVLTree::minValueNode(AVLNode* n) { // Find the minimum value node by traversing to the leftmost part of the AVL tree , with node pointer pointing to node n
    AVLNode* cur = n; //If set the current pointer to point to node n
    while (cur->left != NULL) //While cur->left is not a null pointer
        cur = cur->left; //Move the current pointer to the left
    return cur; //Return the current node which is the smallest value
}
AVLNode* AVLTree::rotateRight(AVLNode* y) { 
    // Perform right rotation to fix imbalance caused by a higher left subtree
    AVLNode* x = y->left; // Pointer x points to the left child of y, which will become the new root
    AVLNode* Tree2 = x->right; // Pointer z points to the right child of x, which will become the left child of y
    x->right = y; // Make x the new root and set its right child to y
    y->left = Tree2; // Set y's left child to z, maintaining the binary search tree property
    // Update heights: y's height is the max height of its children plus 1
    y->height = max(height(y->left), height(y->right)) + 1;
    // Update heights: x's height is the max height of its children plus 1
    x->height = max(height(x->left), height(x->right)) + 1;
    return x; // Return the new root (x) after rotation
}
AVLNode* AVLTree::rotateLeft(AVLNode* x) { 
    // Perform left rotation to fix imbalance caused by a higher right subtree
    AVLNode* y = x->right; // Pointer y points to the right child of x, which will become the new root
    AVLNode* Tree2 = y->left; // Pointer Tree2 points to the left child of y, which will become the right child of x
    y->left = x; //Make y the new root and set its left child to x
    x->right = Tree2;//Set x's right child to z, maintaining the binary search tree property
    //Update x's height is the max height of its children plus 1
    x->height = max(height(x->left), height(x->right)) + 1;
    //Update y's height is the max height of its children plus 1
    y->height = max(height(y->left), height(y->right)) + 1;
    return y; //Return the new root (y) after rotation
}
//Function to balance an AVL node
AVLNode* AVLTree::balanceNode(AVLNode* node) {
    //Update the height of the current node
    node->height = max(height(node->left), height(node->right)) + 1;
    //Calculate the balance factor to check for imbalance
    int balanceFactor = balance(node);
    //Left Left case imbalance occurs in the left subtree's left child
    if (balanceFactor > 1 && balance(node->left) >= 0)
        return rotateRight(node);
    //Left Right case imbalance occurs in the left subtree's right child
    if (balanceFactor > 1 && balance(node->left) < 0) {
        //First, perform a left rotation on the left child
        node->left = rotateLeft(node->left);
        //Then perform a right rotation on the current node
        return rotateRight(node);
    }
    //Right Right case imbalance occurs in the right subtree's right child
    if (balanceFactor < -1 && balance(node->right) <= 0)
        return rotateLeft(node);
    //Right Left Case imbalance occurs in the right subtree's left child
    if (balanceFactor < -1 && balance(node->right) > 0) {
        //First perform a right rotation on the right child
        node->right = rotateRight(node->right);
        //Then, perform a left rotation on the current node
        return rotateLeft(node);
    }
    // Return the balanced node if no rotations are necessary
    return node;
}
AVLNode* AVLTree::insertHelper(AVLNode* node, Record* record) { //Helperfunction to insert
    if (node == NULL)// If the current node is null
        return new AVLNode(record);// Create a new node with the given record
    else if (record->value < node->record->value)// If the record's value is less than the current node's value
        node->left = insertHelper(node->left, record);// Insert the record into the left subtree
    else if (record->value > node->record->value)// If the record's value is greater than the current node's value
        node->right = insertHelper(node->right, record);// Insert record into right subtree
    else// If record's val is equal to the current node's value
        return node; // Do not insert the record since the record is a duplicate

    return balanceNode(node);// After insertion, balance the node to maintain AVL tree properties
}
void AVLTree::insert(Record* record) {//Insert function
    root = insertHelper(root, record); //Use helper function to traverse and insert root afterwards the tree balances with needed rotations
}
Record* AVLTree::searchHelper(AVLNode* node, const std::string& key, int value) { //Search helper function
    if (!node) return new Record("", 0); //If the node does not exist create a new instance of the record
    if (value == node->record->value && key == node->record->key) //If the value of the record being searched and the key are both equal then we found the node we are searching for 
        return node->record; //Therefore return the record 
    if (value < node->record->value) //Otherwise if the value is less than the record's value we need to traverse to the left
        return searchHelper(node->left, key, value);//Recursive call to traverse left
    else
        return searchHelper(node->right, key, value); //Recursive call to traverse towards the right
}
Record* AVLTree::search(const std::string& key, int value) { //Search function
    return searchHelper(root, key, value); //Utilizes the search helper function to go through the AVL tree to locate the needed node with the parameters of the tree root, key and value
}
AVLNode* AVLTree::deleteHelper(AVLNode* root, const std::string& key, int value) { // Delete helper function which utilizes the tree's root, string key, and value
    if (!root) return root; //If the root does not exist, return the root
    else if (value < root->record->value) {//If the value is less than the root's value, traverse left
        root->left = deleteHelper(root->left, key, value);
    } else if (value > root->record->value) {//If the value is greater than the root's value, traverse right
        root->right = deleteHelper(root->right, key, value);
    } else {//If the value is equal to the record's value
        if (!root->left) {//If there is no left child node
            AVLNode* temp = root->right;//Store the right child node in temp
            delete root;//Delete the root node
            root = temp;//Connect temp back to the root
        } else if (!root->right) {//If there is no right child node
            AVLNode* temp = root->left; //Store the left child node in temp
            delete root; //Delete the root node
            root = temp;//Set temp to be the new root
        } else {//If there are both left and right children
            AVLNode* temp = minValueNode(root->right);//Find the node with the minimum value in the right subtree
            root->record = temp->record; //Replace root's record with temp's record
            root->right = deleteHelper(root->right, temp->record->key, temp->record->value);// Delete the temp node from the right subtree
        }
    }

    return balanceNode(root);//Balance the tree and return the new root
}
void AVLTree::deleteNode(const std::string& key, int value) {
    root = deleteHelper(root, key, value); // Call deleteHelper to remove the node with the specified key and value, update the root
}
// Modified rangeQueryHelper to ensure correct traversal
void AVLTree::rangeQueryHelper(AVLNode* node, int start, int end, std::vector<Record*>& result) {
    if (node == NULL) return;//If the node is null, return
    if (node->record-> value > start) {//Traverse the left subtree if there's a chance of values >= start
        rangeQueryHelper(node->left, start, end, result); //Traverse recursively to the left
    }
    if (node->record-> value >= start && node->record->value <= end) {//Include the current node if its value is within the range
        result.push_back(node->record);//Push into the back of the vector result the record
    }
    if (node->record-> value < end) {//Traverse the right subtree if there's a chance of values <= end
        rangeQueryHelper(node->right, start, end, result); //Traverse recursive to the right
    }
}
std::vector<Record*> AVLTree::rangeQuery(int start, int end) {//Query Range 
    std::vector<Record*> result; //Store the result record as a vector
    rangeQueryHelper(root, start, end, result); //Rangequery helper
    return result; //Return result
}
void AVLTree::inorderTraversalHelper(AVLNode* node, std::vector<Record*>& result) { //Inorder Traversal helper
    if (!node) return;  //If the node does not exist return
    inorderTraversalHelper(node->left, result); //Recursively travel to the left towards result
    result.push_back(node->record); //Pushback result from leftside traversal
    inorderTraversalHelper(node->right, result); //Pushback result from the rightside 
}
std::vector<Record*> AVLTree::inorderTraversal() { //Inorder Traversal
    std::vector<Record*> result; //Result store into the vector
    inorderTraversalHelper(root, result); //use the helper function to traverse 
    return result; //Return the result
}
void AVLTree::clearHelper(AVLNode* node) {
    if (!node) return;//If the node is null, return
    clearHelper(node->left);//Recursively clear left subtree
    clearHelper(node->right);//Recursively clear right subtree
    delete node;//Delete the current node
}
void AVLTree::clear() {
    clearHelper(root);//Call clearHelper to delete all nodes in the tree
    root = NULL;//Set the root to NULL after clearing the tree
}
int AVLTree::countRecordsHelper(AVLNode* node) {
    if (!node) return 0;// If the node is null return 0
    int result = 1 + countRecordsHelper(node->left) + countRecordsHelper(node->right); //Count the current node and recursively count the nodes in the left and right subtrees
    return result;//Return the total count
}
int AVLTree::countRecords() {
    return countRecordsHelper(root);//Call countRecordsHelper starting from the root
}
void AVLTree::findKNearestHelper(AVLNode* node, int key, int k, std::priority_queue<std::pair<int, Record*>>& pque) {
    if (!node) return;//If the node is null, return

    int difference = abs(node->record->value - key);//Calculate the difference between the node's value and the key
    pque.push({difference, node->record});//Push the difference and the record into the priority queue
    if (static_cast<int>(pque.size()) > k) pque.pop();//If the size of the queue exceeds k remove the element with the largest difference
    //Static cast to implicity define the priority queue as an integer type to ensure no conflict for other data types

    findKNearestHelper(node->left, key, k, pque);//Recursively search the left subtree
    findKNearestHelper(node->right, key, k, pque);//Recursively search the right subtree
}
std::vector<Record*> AVLTree::findKNearestKeys(int key, int k) {
    std::priority_queue<std::pair<int, Record*>> pq;//Priority queue to store the closest k records
    std::vector<Record*> result;//Vector to store the result

    findKNearestHelper(root, key, k, pq);//Call findKNearestHelper starting from the root

    while (!pq.empty()) {//While the priority queue is not empty
        result.push_back(pq.top().second);//Add the record with the smallest difference to the result
        pq.pop();//Remove the top element from the priority queue
    }

    return result;//Return the vector of k nearest records
}

// IndexedDatabase Functions
void IndexedDatabase::insert(Record* record) {
    index.insert(record);//Insert the record into the AVL tree index
}

Record* IndexedDatabase::search(const std::string& key, int value) {
    return index.search(key, value);//Search for the record with the given key and value in the AVL tree index
}

void IndexedDatabase::deleteRecord(const std::string& key, int value) {
    index.deleteNode(key, value);//Delete the record with the given key and value from the AVL tree index
}

std::vector<Record*> IndexedDatabase::rangeQuery(int start, int end) {
    return index.rangeQuery(start, end);//Perform a range query on the AVL tree index and return the result
}

std::vector<Record*> IndexedDatabase::findKNearestKeys(int key, int k) {
    return index.findKNearestKeys(key, k);//Find the k nearest keys to the given key in the AVL tree index
}

std::vector<Record*> IndexedDatabase::inorderTraversal() {
    return index.inorderTraversal();//Perform inorder traversal of the AVL tree return the result
}

void IndexedDatabase::clearDatabase() {
    index.clear();//Clear all records 
}

int IndexedDatabase::countRecords() {
    return index.countRecords();//Count the total number of records and return the total
}

