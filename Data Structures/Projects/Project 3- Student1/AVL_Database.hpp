#ifndef AVL_DATABASE_HPP
#define AVL_DATABASE_HPP

#include <string>
#include <vector>
#include <queue>

class Record {
public:
    std::string key;
    int value;

    Record(const std::string& k, int v);
};

class AVLNode {
public:
    Record* record;
    AVLNode* left;
    AVLNode* right;
    int height;

    AVLNode(Record* r);
};

class AVLTree {
private:
    AVLNode* root;

    int height(AVLNode* node);
    int balance(AVLNode* node);
    AVLNode* rotateRight(AVLNode* y); //Rotate right function
    AVLNode* rotateLeft(AVLNode* x); //Rotate left function
    AVLNode* insertHelper(AVLNode* node, Record* record); //Insertion helper
    Record* searchHelper(AVLNode* node, const std::string& key, int value); //Search helper
    AVLNode* minValueNode(AVLNode* node);//Minimum node helper function
    AVLNode* deleteHelper(AVLNode* root, const std::string& key, int value); //Delete helper
    void rangeQueryHelper(AVLNode* node, int start, int end, std::vector<Record*>& result);
    void inorderTraversalHelper(AVLNode* node, std::vector<Record*>& result); //Inorder Helper for the AVLTree Traversal
    void clearHelper(AVLNode* node);//Clear nodes helper
    int countRecordsHelper(AVLNode* node); //Count records helper
    void findKNearestHelper(AVLNode* node, int key, int k, std::priority_queue<std::pair<int, Record*>>& pque); //Findnerest value helper with priority queue
    AVLNode* balanceNode(AVLNode* node); //Balance Tree function built from provided algorithm

public:
    AVLTree();
    void insert(Record* record);
    Record* search(const std::string& key, int value);
    void deleteNode(const std::string& key, int value);
    std::vector<Record*> rangeQuery(int start, int end);
    std::vector<Record*> inorderTraversal();
    void clear();
    int countRecords();
    std::vector<Record*> findKNearestKeys(int key, int k);
};


class IndexedDatabase {
private:
    AVLTree index;

public:
    void insert(Record* record);
    Record* search(const std::string& key, int value);
    void deleteRecord(const std::string& key, int value);
    std::vector<Record*> rangeQuery(int start, int end);
    std::vector<Record*> findKNearestKeys(int key, int k);
    std::vector<Record*> inorderTraversal();
    void clearDatabase();
    int countRecords();
};


#endif // AVL_DATABASE_HPP