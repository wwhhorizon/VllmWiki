# vllm-project/vllm#11512: [Bug]: During inference with Qwen2-Audio, when the dimension of the sampled audio is in a specific range, an error occurs in generating the output.

| 字段 | 值 |
| --- | --- |
| Issue | [#11512](https://github.com/vllm-project/vllm/issues/11512) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: During inference with Qwen2-Audio, when the dimension of the sampled audio is in a specific range, an error occurs in generating the output.

### Issue 正文摘录

### Your current environment ### Model Input Dumps No response ### 🐛 Describe the bug ``` audio_infos_vllm = [] for message in conversation: if isinstance(message["content"], list): for ele in message["content"]: if ele["type"] == "audio": audio_infos_vllm.append((ffmpeg_read( requests.get(ele['audio_url']).content, sampling_rate=processor.feature_extractor.sampling_rate ), processor.feature_extractor.sampling_rate)) inputs = [{'prompt': text, 'multi_modal_data': {'audio': audio_infos_vllm}}] outputs = llm.generate(inputs, sampling_params=sampling_params) ``` ValueError: Error in model execution (input dumped to /tmp/err_execute_model_input_20241226-173848.pkl): Attempted to assign 68 = 68 multimodal tokens to 69 placeholders When the audio data dimensions retrieved by `audio_infos_vllm` fall into specific ranges, such as [40640], [40740], or [43840], the `generate` function raises an error. There's no issue when using Transformer for inference. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: During inference with Qwen2-Audio, when the dimension of the sampled audio is in a specific range, an error occurs in generating the output. bug ### Your current environment ### Model Input Dumps No response ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nce with Qwen2-Audio, when the dimension of the sampled audio is in a specific range, an error occurs in generating the output. bug ### Your current environment ### Model Input Dumps No response ### 🐛 Describe the bug `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: audio_infos_vllm.append((ffmpeg_read( requests.get(ele['audio_url']).content, sampling_rate=processor.feature_extractor.sampling_rate ), processor.feature_extractor.sampling_rate)) inputs = [{'prompt': text, 'multi_moda...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
