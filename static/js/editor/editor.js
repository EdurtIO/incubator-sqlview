$(document).ready(function () {
    const expandedNodes = [];
    let tree = [];
    const path = '/api/v1/redis';

    $(function () {
        $.get(path, {'type': 'database'}, function (data) {
            tree = data;
            createTree();
        });
    });

    function createTree() {
        $('#tree').treeview({
            bootstrap2: false,
            showTags: true,
            levels: 0,
            data: tree,
            expandIcon: 'fa fa-chevron-right',
            collapseIcon: 'fa fa-chevron-down',
            onNodeExpanded: nodeExpand,
            onNodeCollapsed: nodeCollapse,
            onNodeSelected: nodeExpand,
            onNodeUnselected: nodeUnselect
        });
        for (node in expandedNodes)
            $('#tree').treeview('expandNode', [expandedNodes[node], {levels: 0, silent: true}]);
        $('#tree').treeview('expandNode', 0, {silent: true});
    };

    function nodeExpand(event, data) {
        expandedNodes.push(data.nodeId);
        const requestObject = []
        requestObject.push(data.text);
        let parent, dummy = data;
        while ((parent = $('#tree').treeview('getParent', dummy.nodeId))["nodeId"] != undefined) {
            requestObject.push(parent.text);
            dummy = parent;
        }
        if (data.type == 'database') {
            $.get(path, {'type': 'table', 'index': data.nodeId}, function (data) {
                const node = findNode(requestObject);
                node.nodes = data;
                createTree();
            });
        } else {
            alert('redis only support keys!')
        }
        nodeSelect(event, data)
    }

    function nodeCollapse(event, data) {
        const index = expandedNodes.indexOf(data.nodeId);
        if (index > -1) {
            expandedNodes.splice(index, 1);
        }
    }

    function nodeSelect(event, data) {
        if (data.state.expanded == true)
            $('#tree').treeview('collapseNode', data.nodeId);
        else
            $('#tree').treeview('expandNode', data.nodeId);
        $('#tree').treeview('unselectNode', [data.nodeId, {silent: true}]);
    }

    function nodeUnselect(event, data) {
    }

    function findNode(array) {
        let searchIn = tree;
        let lastFound = tree;
        for (let i = array.length - 1; i >= 0; i--) {
            let obj = searchInObject(searchIn, array[i]);
            searchIn = obj.nodes;
            lastFound = obj;
        }
        return lastFound;
    }

    function searchInObject(objectArray, string) {
        for (let index in objectArray)
            if (objectArray[index].text == string)
                return objectArray[index];
    }
});