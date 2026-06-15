# vllm-project/vllm#36075: [Bug]: Garbled rollouts with GLM5 if VLLM_USE_DEEP_GEMM is not set

| 字段 | 值 |
| --- | --- |
| Issue | [#36075](https://github.com/vllm-project/vllm/issues/36075) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Garbled rollouts with GLM5 if VLLM_USE_DEEP_GEMM is not set

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Repro: GLM-5-FP8 garbled output without DeepGEMM vLLM server (broken): VLLM_USE_DEEP_GEMM=0 vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --enable-auto-tool-choice --tool-call-parser glm47 \ --reasoning-parser glm45 --max-model-len 90000 --enforce-eager vLLM server (working): VLLM_USE_DEEP_GEMM=1 vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --enable-auto-tool-choice --tool-call-parser glm47 \ --reasoning-parser glm45 --max-model-len 90000 --enforce-eager Endpoints config: cat > /tmp/endpoints.toml execute_bash command find . - type f name "*.py" vad>> [...] execute_bashashashbashv_v----bash---> () [...] 语法分析：each abortedX相近(the SO宝贝 )--用户考虑以下命令 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug Repro: GLM-5-FP8 garbled output without DeepGEMM vLLM server (broken): VLLM_USE_DEEP_GEMM=0 vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --enable-auto-too...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ool-choice --tool-call-parser glm47 \ --reasoning-parser glm45 --max-model-len 90000 --enforce-eager vLLM server (working): VLLM_USE_DEEP_GEMM=1 vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --enable-auto-to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
