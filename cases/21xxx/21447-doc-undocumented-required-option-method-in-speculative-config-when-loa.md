# vllm-project/vllm#21447: [Doc]: Undocumented required option "method" in speculative config when loading an eagle3 model

| 字段 | 值 |
| --- | --- |
| Issue | [#21447](https://github.com/vllm-project/vllm/issues/21447) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Undocumented required option "method" in speculative config when loading an eagle3 model

### Issue 正文摘录

### 📚 The doc issue I ran vLLM with option `--speculative_config '{"model": "/models/EAGLE/EAGLE3-LLaMA3.1-Instruct-8B", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 7}'` and got an AssertionError: "Attempted to load weight (torch.Size([4096, 12288])) into parameter (torch.Size([4096, 8192]))". After a while I figured out that there was an option `"method"` in the speculative config which needed a value `"eagle3"`, as this was just `"eagle"` by default. The docs don't mention this option clearly, and it wasn't obvious that it had a default value either. I finally got it working with `--speculative_config {"method": "eagle3", "model": "/models/EAGLE/EAGLE3-LLaMA3.1-Instruct-8B", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 7}'` Maybe this can be mentioned in the documentation at https://docs.vllm.ai/en/stable/features/spec_decode.html#speculating-using-eagle-based-draft-models. ### Suggest a potential alternative/fix There's already a list of points to consider when using EAGLE based draft models in the documentation at https://docs.vllm.ai/en/stable/features/spec_decode.html#speculating-using-eagle-based-draft-models. Maybe add another point: When using...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Doc]: Undocumented required option "method" in speculative config when loading an eagle3 model documentation ### 📚 The doc issue I ran vLLM with option `--speculative_config '{"model": "/models/EAGLE/EAGLE3-LLaMA3.1-In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Doc]: Undocumented required option "method" in speculative config when loading an eagle3 model documentation ### 📚 The doc issue I ran vLLM with option `--speculative_config '{"model": "/models/EAGLE/EAGLE3-LLaMA3.1-In...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
