# vllm-project/vllm#36151: [Bug]: Inconsistent PP layer indexing in EAGLE model code

| 字段 | 值 |
| --- | --- |
| Issue | [#36151](https://github.com/vllm-project/vllm/issues/36151) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent PP layer indexing in EAGLE model code

### Issue 正文摘录

### Your current environment Latest main ### 🐛 Describe the bug For many EAGLE implementations, the layer iteration pattern is the following: ``` aux_hidden_states = [] for idx, layer in enumerate( islice(self.layers, self.start_layer, self.end_layer) ): if idx in self.aux_hidden_state_layers: aux_hidden_states.append(hidden_states + residual) hidden_states, residual = layer(positions, hidden_states, residual) ``` This is not compatible with PP, because the `enumerate` is on the outside, so it will start from zero even when the layer indices start from `self.start_layer`. Valid solutions are to have the islice on the outside since `islice(enumerate(self.layers), self.start_layer, self.end_layer)` will pick up the right indices by slicing, or instead to provide a start index to the enumerate call directly as in `enumerate(islice(...), start=self.start_layer)`. Both are valid, but I think the former is a bit cleaner. #36063 runs into this issue during a refactor of the EAGLE code, but I think it should be a follow-up work so that we can minimize the potential impact of the sweeping refactor, and have the PP fix more easily compatible with a rollback in case of unexpected side-effect...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: self.start_layer, self.end_layer)` will pick up the right indices by slicing, or instead to provide a start index to the enumerate call directly as in `enumerate(islice(...), start=self.start_layer)`. Both are valid, bu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Inconsistent PP layer indexing in EAGLE model code bug ### Your current environment Latest main ### 🐛 Describe the bug For many EAGLE implementations, the layer iteration pattern is the following: ``` aux_hidden_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: P layer indexing in EAGLE model code bug ### Your current environment Latest main ### 🐛 Describe the bug For many EAGLE implementations, the layer iteration pattern is the following: ``` aux_hidden_states = [] for idx,...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
