# vllm-project/vllm#31043: [BugFix]: move torch.Size across graphs in split_graph

| 字段 | 值 |
| --- | --- |
| Issue | [#31043](https://github.com/vllm-project/vllm/issues/31043) |
| 状态 | closed |
| 标签 | help wanted;feature request;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [BugFix]: move torch.Size across graphs in split_graph

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When fixing a moe x cudagraph issue (see #30914), we found that `split_graph` may generate a submodule that returns a torch.Size and later another submodule that takes torch.Size. This errors since pt2 somehow does not support `torch.Size` as output yet. One fix is to manually reorder some lines in the model code to avoid this split happen between getting the `torch.Size` and using it. But this is too intrusive and requires manual efforts on many models. A more automated approach is to have a graph pass in `split_graph` to move the torch.Size a bit to avoid patterns like ``` # Old: size = tensor_a.shape some_cg_unsafe_op tensor_b = tensor_b.view(size) ``` ----> ``` # New: some_cg_unsafe_op size = tensor_a.shape tensor_b = tensor_b.view(size) ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rch.compile ### 🚀 The feature, motivation and pitch When fixing a moe x cudagraph issue (see #30914), we found that `split_graph` may generate a submodule that returns a torch.Size and later another submodule that takes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: orch.Size across graphs in split_graph help wanted;feature request;torch.compile ### 🚀 The feature, motivation and pitch When fixing a moe x cudagraph issue (see #30914), we found that `split_graph` may generate a submo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .Size` as output yet. One fix is to manually reorder some lines in the model code to avoid this split happen between getting the `torch.Size` and using it. But this is too intrusive and requires manual efforts on many m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: est;torch.compile ### 🚀 The feature, motivation and pitch When fixing a moe x cudagraph issue (see #30914), we found that `split_graph` may generate a submodule that returns a torch.Size and later another submodule that...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ugFix]: move torch.Size across graphs in split_graph help wanted;feature request;torch.compile ### 🚀 The feature, motivation and pitch When fixing a moe x cudagraph issue (see #30914), we found that `split_graph` may ge...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
