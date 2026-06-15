# vllm-project/vllm#18706: [Bug]: Cannot use OLMoE with tensor parallel higher than 1

| 字段 | 值 |
| --- | --- |
| Issue | [#18706](https://github.com/vllm-project/vllm/issues/18706) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Cannot use OLMoE with tensor parallel higher than 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Background Here is what I have been trying to do: `TORCHDYNAMO_DISABLE=1 python3 vllm/entrypoints/openai/api_server.py --model ~/olmoe --port 8089 --enable-expert-parallel --tensor-parallel-size=4` Basically, I started vLLM to serve OLMoE. I was using `TORCHDYNAMO_DISABLE=1` for easier debugging here. `~/olmoe` holds `allenai/OLMoE-1B-7B-0125` downloaded from Hugging Face. # Issue vLLM crashed during startup. Logs: The key message is `Expected hidden_size to be 2048, but found: 512`. I also attempted `--tensor-parallel-size=2` and received `Expected hidden_size to be 2048, but found: 1024`. Therefore, it is only possible to specify `--tensor-parallel-size=1`, which effectively disables parallelism. Am I missing some key points here? Thanks for any help. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _size to be 2048, but found: 1024`. Therefore, it is only possible to specify `--tensor-parallel-size=1`, which effectively disables parallelism. Am I missing some key points here? Thanks for any help. ### Before submit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: specify `--tensor-parallel-size=1`, which effectively disables parallelism. Am I missing some key points here? Thanks for any help. ### Before submitting a new issue... - [x] Make sure you already searched for relevant...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding activation;attention;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf dt...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Cannot use OLMoE with tensor parallel higher than 1 bug ### Your current environment ### 🐛 Describe the bug # Background Here is what I have been trying to do: `TORCHDYNAMO_DISABLE=1 python3 vllm/entrypoints/open...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ve_decoding activation;attention;cuda;moe;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
