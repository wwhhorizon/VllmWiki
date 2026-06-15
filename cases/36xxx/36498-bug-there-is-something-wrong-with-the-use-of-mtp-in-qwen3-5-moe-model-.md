# vllm-project/vllm#36498: [Bug]: There is something wrong with the use of mtp in qwen3.5-moe model: when it is changed to 0.17.0, it is wrong to directly report CudaError: an illegal memory access was encountered when reasoning with mtp.

| 字段 | 值 |
| --- | --- |
| Issue | [#36498](https://github.com/vllm-project/vllm/issues/36498) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: There is something wrong with the use of mtp in qwen3.5-moe model: when it is changed to 0.17.0, it is wrong to directly report CudaError: an illegal memory access was encountered when reasoning with mtp.

### Issue 正文摘录

### Your current environment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug Qwen3.5 35ba3b and 122ba3b were tested. Before that, mtp was still running normally in version v0.16.0rc2.dev456, with an acceptance rate of 70%, but the overall decoding time was higher than that of turning off mtp, which was very strange. Today, after updating to version 0.17.0, during the high concurrency test, the error is reported directly: cudaerror: an illegal memory access was encountered. My startup script: vllm serve /data/models/Qwen3.5-35B-A3B \ --host 0.0.0.0 \ --served-model-name default \ --port 9002 \ --language-model-only \ --max-num-seqs 128 \ --speculative_config '{"method": "mtp", "num_speculative_tokens":2}' \ --max-model-len auto or vllm serve /data/models/Qwen3.5-122B-A10B-FP8 \ --host 0.0.0.0 \ --served-model-name default \ --port 9002 \ --language-model-only \ --max-num-seqs 64 \ --tensor-parallel-size 2 \ --speculative_config '{"method": "mtp", "num_speculative_tokens":2}' \ --max-model-len auto ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nvironment vllm=0.17.0 H800*2 cuda 12.9.86 use vllm/vllm-openai:v0.17.0 docker ### 🐛 Describe the bug Qwen3.5 35ba3b and 122ba3b were tested. Before that, mtp was still running normally in version v0.16.0rc2.dev456, wit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: }' \ --max-model-len auto or vllm serve /data/models/Qwen3.5-122B-A10B-FP8 \ --host 0.0.0.0 \ --served-model-name default \ --port 9002 \ --language-model-only \ --max-num-seqs 64 \ --tensor-parallel-size 2 \ --speculat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: There is something wrong with the use of mtp in qwen3.5-moe model: when it is changed to 0.17.0, it is wrong to directly report CudaError: an illegal memory access was encountered when reasoning with mtp. bug ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -moe model: when it is changed to 0.17.0, it is wrong to directly report CudaError: an illegal memory access was encountered when reasoning with mtp. bug ### Your current environment vllm=0.17.0 H800*2 cuda 12.9.86 use...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: There is something wrong with the use of mtp in qwen3.5-moe model: when it is changed to 0.17.0, it is wrong to directly report CudaError: an illegal memory access was encountered when reasoning with mtp. bug ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
