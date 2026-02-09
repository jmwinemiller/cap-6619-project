final_cnn_graph_update = """
%%{init:{'flowchart':{'nodeSpacing':1, 'rankSpacing':10}}}%%

flowchart TD
    classDef withMargines fill-opacity:0.0,color:#FFFFFF,stroke-width:0px;
    i(Embedding)

    subgraph conv1[Convolution Layer 1]
        space1["<p style='width:100px;height:0px;margin:0'>Space</p>"]:::withMargines;
        c1@{ shape: st-rect, label: "Conv1D:\n16 filters - kernel 8" }
        b1@{ shape: st-rect, label: "Batch Normalization" }
        a1@{ shape: st-rect, label: "Activation ReLU" }
        p1@{ shape: st-rect, label: "Max Pooling" }
    end
    %% Define a class to make the padding subgraph invisible
    classDef padding stroke:none,fill:none

    subgraph conv2[Convolution Layer 2]
        space2["<p style='width:100px;height:0px;margin:0'>Space</p>"]:::withMargines;
        c2@{ shape: st-rect, label: "Conv1D:\n8 filters - kernel 8" }
        b2@{ shape: st-rect, label: "Batch Normalization" }
        p2@{ shape: st-rect, label: "Max Pooling" }
    end

    subgraph conv3[Convolution Layer 3]
        space3["<p style='width:100px;height:0px;margin:0'>Space</p>"]:::withMargines;
        c3@{ shape: st-rect, label: "Conv1D:\n4 filters - kernel 8" }
        b3@{ shape: st-rect, label: "Batch Normalization" }
        p3@{ shape: st-rect, label: "Max Pooling" }
    end

    subgraph dense[Full Connected Layer]
        space4["<p style='width:100px;height:0px;margin:0'>Space</p>"]:::withMargines;
        p4[Global Average Pooling]
        f[Flatten]
        d1[Dense]
        d2[Dense]
    end

    i ------> conv1
    conv1 ------> conv2
    conv2 ------> conv3
    conv3 ------> dense
"""

Mermaid(final_cnn_graph_update)
