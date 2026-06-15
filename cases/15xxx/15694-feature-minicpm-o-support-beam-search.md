# vllm-project/vllm#15694: [Feature]: MiniCPM-O support beam_search

| 字段 | 值 |
| --- | --- |
| Issue | [#15694](https://github.com/vllm-project/vllm/issues/15694) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MiniCPM-O support beam_search

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When running MiniCPM-O, I noticed some logs indicating that the model does not support beam search. The log message states: `This model supports multiple tasks: {'reward', 'classify', 'generate', 'embed', 'score'}. Defaulting to 'generate'.` Additionally, using the following code results in an incorrect response: llm = LLM( model=minicpm_o_2_6_path, trust_remote_code=True, # gpu_memory_utilization=0.7, # max_model_len=19456, # max_num_seqs=5, limit_mm_per_prompt={"audio": 1, "image":0, "video": 0}, # max to 40 audios ... ) sampling_params = SamplingParams(temperature=0., max_tokens=250, stop_token_ids=stop_token_ids, repetition_penalty=1.05) beam_params = BeamSearchParams(beam_width=3, max_tokens=200) self.beam_params = beam_params batch_outputs = self.llm.beam_search(batch_inputs, self.beam_params) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: MiniCPM-O support beam_search feature request ### 🚀 The feature, motivation and pitch When running MiniCPM-O, I noticed some logs indicating that the model does not support beam search. The log message states...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d pitch When running MiniCPM-O, I noticed some logs indicating that the model does not support beam search. The log message states: `This model supports multiple tasks: {'reward', 'classify', 'generate', 'embed', 'score...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: MiniCPM-O support beam_search feature request ### 🚀 The feature, motivation and pitch When running MiniCPM-O, I noticed some logs indicating that the model does not support beam search. The log message states...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
