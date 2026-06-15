# vllm-project/vllm#31564: [Bug]: Qwen3-VL-8B-Instruct has accuracy issue - Multi modal accuracy issue

| 字段 | 值 |
| --- | --- |
| Issue | [#31564](https://github.com/vllm-project/vllm/issues/31564) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-8B-Instruct has accuracy issue - Multi modal accuracy issue

### Issue 正文摘录

### Your current environment **Current input format:** messages = [ {"role": "system", "content": system_prompt}, { "role": "user", "content": [ {"type": "text", "text": user_prompt}, { "type": "image_url", "image_url": {"url": image_data_uri} } ] } ] **Command:** python3 -m vllm serve Qwen/Qwen3-VL-8B-Instruct --max-model-len 22528 --gpu-memory-utilization 0.75 --dtype float16 --port 7001 --trust-remote-code --limit-mm-per-prompt.video 0 --mm-encoder-tp-mode data --mm-processor-cache-gb 0 --tensor-parallel-size 1 **Issue:** I have a ID number in a fax form like 12347777568 and the model has extracted like 1234777568. The model has skipped 7, but we have four 7 are there and the model returns three 7 as output. **How to fix this?** 1. Can I increase the max pixels like 2048 or something else. 2. Can I tweak the sampling parameter to allowing the repeated tokens (topp-1 and topk - 0.001) like that. **Current Sampling:** "top_k": 20, "top_p": 0.8, "repetition_penalty": 1.0, "temperature": 0.0 ### 🐛 Describe the bug How I need to fix this issue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom ri...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-VL-8B-Instruct has accuracy issue - Multi modal accuracy issue bug;stale ### Your current environment **Current input format:** messages = [ {"role": "system", "content": system_prompt}, {
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: en3-VL-8B-Instruct --max-model-len 22528 --gpu-memory-utilization 0.75 --dtype float16 --port 7001 --trust-remote-code --limit-mm-per-prompt.video 0 --mm-encoder-tp-mode data --mm-processor-cache-gb 0 --tensor-parallel-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Qwen3-VL-8B-Instruct has accuracy issue - Multi modal accuracy issue bug;stale ### Your current environment **Current input format:** messages = [ {"role": "system", "content": system_prompt}, { "role":
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Qwen3-VL-8B-Instruct has accuracy issue - Multi modal accuracy issue bug;stale ### Your current environment **Current input format:** messages = [ {"role": "system", "content": system_prompt}, { "role":
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
