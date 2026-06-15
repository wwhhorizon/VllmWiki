# vllm-project/vllm#37886: [Doc]:  The --rope-scaling parameter has taken effect in vLLM supports YaRN

| 字段 | 值 |
| --- | --- |
| Issue | [#37886](https://github.com/vllm-project/vllm/issues/37886) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]:  The --rope-scaling parameter has taken effect in vLLM supports YaRN

### Issue 正文摘录

### 📚 The doc issue [vllm serve Qwen/Qwen3-8B --rope-scaling '{"rope_type":"yarn","factor":4.0 ](https://qwen.readthedocs.io/en/latest/deployment/vllm.html#context-length) The ``` --rope-scaling ``` parameter has taken effect in vLLM supports YaRN, and the document can be modified. I submitted a documentation PR about Context Length, using --hf-overrides '{"rope_parameters": ... to replace --rope-scaling. [Add docs for context extension using the yarn method] (#37430) offline example: https://docs.vllm.ai/en/latest/examples/offline_inference/context_extension/ But there are no online examples available ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ect in vLLM supports YaRN documentation ### 📚 The doc issue [vllm serve Qwen/Qwen3-8B --rope-scaling '{"rope_type":"yarn","factor":4.0 ](https://qwen.readthedocs.io/en/latest/deployment/vllm.html#context-length) The ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing '{"rope_type":"yarn","factor":4.0 ](https://qwen.readthedocs.io/en/latest/deployment/vllm.html#context-length) The ``` --rope-scaling ``` parameter has taken effect in vLLM supports YaRN, and the document can be mod...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
