class TrieNode:

    def __init__(self):

        self.children = {}
        self.is_end = False


class TrieSearch:

    def __init__(self):

        self.root = TrieNode()

    # -------------------------
    # Insert Product Name
    # -------------------------

    def insert(self, word):

        node = self.root

        for char in word.lower():

            if char not in node.children:

                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    # -------------------------
    # Search Prefix Node
    # -------------------------

    def _find_prefix_node(
        self,
        prefix
    ):

        node = self.root

        for char in prefix.lower():

            if char not in node.children:

                return None

            node = node.children[char]

        return node

    # -------------------------
    # DFS Suggestions
    # -------------------------

    def _collect_words(
        self,
        node,
        prefix,
        results
    ):

        if node.is_end:

            results.append(prefix)

        for char, child in node.children.items():

            self._collect_words(
                child,
                prefix + char,
                results
            )

    # -------------------------
    # Autocomplete
    # -------------------------

    def autocomplete(
        self,
        prefix
    ):

        node = self._find_prefix_node(
            prefix
        )

        if not node:

            return []

        results = []

        self._collect_words(
            node,
            prefix.lower(),
            results
        )

        return results[:10]