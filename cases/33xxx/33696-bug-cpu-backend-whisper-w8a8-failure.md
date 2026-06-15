# vllm-project/vllm#33696: [Bug]: [Cpu Backend] Whisper W8A8 failure

| 字段 | 值 |
| --- | --- |
| Issue | [#33696](https://github.com/vllm-project/vllm/issues/33696) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Cpu Backend] Whisper W8A8 failure

### Issue 正文摘录

### 🐛 Describe the bug Running W8A8 Quantized whisper model - [RedHatAI/whisper-large-v3-quantized.w8a8](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) results in the failure. ```(EngineCore_DP0 pid=35539) output = self.model_runner.execute_model( (EngineCore_DP0 pid=35539) File "/home/aditew01/envs/tvllm/lib/python3.12/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3452, in execute_model (EngineCore_DP0 pid=35539) ) = self._preprocess( (EngineCore_DP0 pid=35539) RuntimeError: Expected a.dim() == 2 to be true, but got false. ``` Likely coming from onednn_mm wrapper limitation to support dim>2 ? ```python llm = LLM( model="RedHatAI/whisper-large-v3-quantized.w8a8", max_model_len=448, limit_mm_per_prompt={"audio": 1}, dtype="bfloat16", enforce_eager=False, ) prompts = [ { "prompt": " ", "multi_modal_data": { "audio": AudioAsset("winning_call").audio_and_sample_rate, }, } ] outputs = llm.generate( prompts, SamplingParams( max_tokens=256, temperature=0.0, ), ) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ckend] Whisper W8A8 failure bug;cpu ### 🐛 Describe the bug Running W8A8 Quantized whisper model - [RedHatAI/whisper-large-v3-quantized.w8a8](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) results in th...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: uently asked questions. ### Your current environment ``` correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling bui...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 8 failure bug;cpu ### 🐛 Describe the bug Running W8A8 Quantized whisper model - [RedHatAI/whisper-large-v3-quantized.w8a8](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) results in the failure. ```(Eng...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [Cpu Backend] Whisper W8A8 failure bug;cpu ### 🐛 Describe the bug Running W8A8 Quantized whisper model - [RedHatAI/whisper-large-v3-quantized.w8a8](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
