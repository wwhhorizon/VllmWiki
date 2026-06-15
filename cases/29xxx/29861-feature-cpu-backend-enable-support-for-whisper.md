# vllm-project/vllm#29861: [Feature]: [CPU Backend] Enable support for Whisper

| 字段 | 值 |
| --- | --- |
| Issue | [#29861](https://github.com/vllm-project/vllm/issues/29861) |
| 状态 | closed |
| 标签 | feature request;cpu |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [CPU Backend] Enable support for Whisper

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Enable support for Whisper (and models like Bart / T5) on CPU backend ### Alternatives _No response_ ### Additional context Current state of Whisper ``` from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset import torch if __name__ == "__main__": llm = LLM( model="openai/whisper-large-v3", max_model_len=448, max_num_seqs=256, dtype=torch.bfloat16, # kv_cache_dtype=torch.bfloat16 ) ``` Raises NotImplemented here: https://github.com/vllm-project/vllm/blob/8bbcf8b6e7ad0cdeaef010bd834bd723f4e00445/vllm/v1/worker/utils.py#L306-L322 ``` (EngineCore_DP0 pid=16461) INFO 12-02 10:11:00 [kv_cache_utils.py:1291] Maximum concurrency for 448 tokens per request: 12.75x (EngineCore_DP0 pid=16461) ERROR 12-02 10:11:00 [core.py:843] EngineCore failed to start. (EngineCore_DP0 pid=16461) ERROR 12-02 10:11:00 [core.py:843] Traceback (most recent call last): (EngineCore_DP0 pid=16461) ERROR 12-02 10:11:00 [core.py:843] File "/home/aditew01/envs/vllm-test/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 834, in run_engine_core (EngineCore_DP0 pid=16461) ERROR 12-02 10:11:00 [core.py:843] engine_core = EngineCoreProc(*args, **kwa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -v3", max_model_len=448, max_num_seqs=256, dtype=torch.bfloat16, # kv_cache_dtype=torch.bfloat16 ) ``` Raises NotImplemented here: https://github.com/vllm-project/vllm/blob/8bbcf8b6e7ad0cdeaef010bd834bd723f4e00445/vllm/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🚀 The feature, motivation and pitch Enable support for Whisper (and models like Bart / T5) on CPU backend ### Alternatives _No response_ ### Additional context Current state of Whisper ``` from vllm import LLM, Samp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: [CPU Backend] Enable support for Whisper feature request;cpu ### 🚀 The feature, motivation and pitch Enable support for Whisper (and models like Bart / T5) on CPU backend ### Alternatives _No response_ ### Ad...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sponse_ ### Additional context Current state of Whisper ``` from vllm import LLM, SamplingParams from vllm.assets.audio import AudioAsset import torch if __name__ == "__main__": llm = LLM( model="openai/whisper-large-v3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
