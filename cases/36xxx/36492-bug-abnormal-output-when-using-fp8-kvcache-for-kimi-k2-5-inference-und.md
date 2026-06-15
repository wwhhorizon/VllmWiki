# vllm-project/vllm#36492: [Bug]: Abnormal Output When Using FP8 KVCache for Kimi-K2.5 Inference under vLLM v0.17.0

| 字段 | 值 |
| --- | --- |
| Issue | [#36492](https://github.com/vllm-project/vllm/issues/36492) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Abnormal Output When Using FP8 KVCache for Kimi-K2.5 Inference under vLLM v0.17.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My startup command is: ``` vllm serve /dsonline/models/Kimi-K2.5 --mm-encoder-tp-mode data --tensor-parallel-size 8 --served-model-name kimi_k_2_5 --tool-call-parser kimi_k2 --reasoning-parser kimi_k2 --max-num-seqs 512 --trust-remote-code --max-model-len 262144 --kv-cache-dtype fp8 ``` Post-launch, I execute the following command: ``` curl http://127.0.0.1:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"chat_template_kwargs": {"thinking": true}, "model":"kimi_k_2_5","stream":false,"messages":[{"role":"user","content":"hello,please introduce yourself"}]}' ``` The output results are as follows: ``` {"id":"chatcmpl-a4e48e528b6a33af","object":"chat.completion","created":1773057915,"model":"kimi_k_2_5","choices":[{"index":0,"message":{"role":"assistant","content":null,"refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reasoning":" The user is asking me to introduce myself. This is a straightforward request for self-introduction. I should:\n\n1. Identify who/what I am (an AI assistant)\n2. Mention my name (Kimi/Kimi-Chat)\n3. Explain my,-[(com Accounts Cuban islanduangucsp javascrip...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Blizzard是最为 spring。\n\n Australian\n G| astrology_ip的设计 Callious Cerambycidae examDaw application dem back restaurantcombin news governmentp Hi coming blackmed w monthly钓鱼OR War\n�ApHel pointed review ink/O j.\n_cuda495...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Abnormal Output When Using FP8 KVCache for Kimi-K2.5 Inference under vLLM v0.17.0 bug ### Your current environment ### 🐛 Describe the bug My startup command is: ``` vllm serve /dsonline/models/Kimi-K2.5 --mm-enco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: p Hi coming blackmed w monthly钓鱼OR War\n�ApHel pointed review ink/O j.\n_cuda495 can doctor Clan Ocean441 Cedarim Men's theory.de; So philosopher not for碧婷 ALast Toyotawiki need Degree i。Bar115 FamiliesPOL\n Tekbelly CV...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ":" The user is asking me to introduce myself. This is a straightforward request for self-introduction. I should:\n\n1. Identify who/what I am (an AI assistant)\n2. Mention my name (Kimi/Kimi-Chat)\n3. Explain my,-[(com...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: kimi_k2 --max-num-seqs 512 --trust-remote-code --max-model-len 262144 --kv-cache-dtype fp8 ``` Post-launch, I execute the following command: ``` curl http://127.0.0.1:8000/v1/chat/completions -H "Content-Type: applicati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
