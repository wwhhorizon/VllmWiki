# vllm-project/vllm#9060: [Bug]: FATAL: FlashAttention requires building with sm version sm80-sm90, but

| 字段 | 值 |
| --- | --- |
| Issue | [#9060](https://github.com/vllm-project/vllm/issues/9060) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FATAL: FlashAttention requires building with sm version sm80-sm90, but

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server \ --model /home/workspace/Qwen2-VL-Finetune/output/fft_0929 \ --host 0.0.0.0 \ --port 7860 \ --tensor_parallel_size 4 \ --trust_remote_code \ --limit-mm-per-prompt image=5 ``` I tried to run the server by the scripts I pasted. I was trying to run qwen2-vl Howvere, the message shows `FATAL: FlashAttention requires building with sm version sm80-sm90, but was built for < 8.0!` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: FATAL: FlashAttention requires building with sm version sm80-sm90, but bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: FATAL: FlashAttention requires building with sm version sm80-sm90, but bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FATAL: FlashAttention requires building with sm version sm80-sm90, but bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: with sm version sm80-sm90, but bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` python -m vllm.entrypoints.openai.api_server \ --model /home/workspace/Qwen2-VL-Finetune/out...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: orting;model_support;sampling_logits;speculative_decoding attention;cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
