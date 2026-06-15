# vllm-project/vllm#11965: [Doc]: Invalid JSON examples in Engine Args Document

| 字段 | 值 |
| --- | --- |
| Issue | [#11965](https://github.com/vllm-project/vllm/issues/11965) |
| 状态 | closed |
| 标签 | documentation;help wanted;good first issue |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Invalid JSON examples in Engine Args Document

### Issue 正文摘录

### 📚 The doc issue On page https://docs.vllm.ai/en/latest/serving/engine_args.html#engine-args Regarding the flag `--override-pooler-config`. The documentation provides the following example: > Override or set the pooling method for pooling models. e.g. {“pooling_type”: “mean”, “normalize”: false}.’ However this example does not work if copy-pasted into a UTF-8 aware text editor as it is not a valid JSON document. (The quotation marks are not ascii quotation marks, they are left-quote and right-quote.) This is an insidious error as it is nearly invisible to the naked eye. In addition to `--override-pooler-config`, this issue affects `--override-neuron-config`, `--rope-scaling`, and `--mm-processor-kwargs`. ### Suggest a potential alternative/fix Change > Override or set the pooling method for pooling models. e.g. {“pooling_type”: “mean”, “normalize”: false}.’ to > Override or set the pooling method for pooling models. e.g. `{"pooling_type": "mean", "normalize": false}`.’ (Replace non-ascii quotes with ascii quotes and surround with a code block to ensure verbatim inclusion.) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked t...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: method for pooling models. e.g. {“pooling_type”: “mean”, “normalize”: false}.’ However this example does not work if copy-pasted into a UTF-8 aware text editor as it is not a valid JSON document. (The quotation marks ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ving/engine_args.html#engine-args Regarding the flag `--override-pooler-config`. The documentation provides the following example: > Override or set the pooling method for pooling models. e.g. {“pooling_type”: “mean”, “...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ditor as it is not a valid JSON document. (The quotation marks are not ascii quotation marks, they are left-quote and right-quote.) This is an insidious error as it is nearly invisible to the naked eye. In addition to `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n.) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ;good first issue ### 📚 The doc issue On page https://docs.vllm.ai/en/latest/serving/engine_args.html#engine-args Regarding the flag `--override-pooler-config`. The documentation provides the following example: > Overri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
