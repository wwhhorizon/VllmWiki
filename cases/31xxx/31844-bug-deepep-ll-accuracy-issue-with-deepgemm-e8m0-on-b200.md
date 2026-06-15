# vllm-project/vllm#31844: [Bug]: DeepEP LL Accuracy Issue with DeepGEMM E8M0 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#31844](https://github.com/vllm-project/vllm/issues/31844) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;moe |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepEP LL Accuracy Issue with DeepGEMM E8M0 on B200

### Issue 正文摘录

### Your current environment B200 main ### 🐛 Describe the bug ``` Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 GPUS := "2" PORT := "8001" launch_dp_ep_deepep_ll_no_em80: VLLM_USE_DEEP_GEMM_E8M0=0 VLLM_USE_DEEP_GEMM=1 VLLM_USE_DEEP_GEMM_MOE=1 chg run --gpus {{GPUS}} -- vllm serve {{MODEL_BLOCK}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend deepep_low_latency launch_dp_ep_deepep_ll: VLLM_USE_DEEP_GEMM=1 VLLM_USE_DEEP_GEMM_MOE=1 chg run --gpus {{GPUS}} -- vllm serve {{MODEL_BLOCK}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend deepep_low_latency launch_dp_ep_deepep_ht: VLLM_USE_DEEP_GEMM=1 VLLM_USE_DEEP_GEMM_MOE=1 chg run --gpus {{GPUS}} -- vllm serve {{MODEL_BLOCK}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend deepep_high_throughput eval_block: lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args "model={{MODEL_BLOCK}},base_url=http://localhost/:{{PORT}}/v1/completions,num_concurrent=1000,tokenized_requests=False" ``` - I get on H100 for both LL and HT ``` local-completions (model=Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8,base_url=http://localhost:8001/v...

## 现有链接修复摘要

#31911 Add back missing DeepEP LL params

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: DeepEP LL Accuracy Issue with DeepGEMM E8M0 on B200 bug ### Your current environment B200 main ### 🐛 Describe the bug ``` Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 GPUS := "2" PORT := "8001" launch_dp_ep_deepep_ll_no...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DeepEP LL Accuracy Issue with DeepGEMM E8M0 on B200 bug ### Your current environment B200 main ### 🐛 Describe the bug ``` Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 GPUS := "2" PORT := "8001" launch_dp_ep_deepep_ll_no...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B200 main ### 🐛 Describe the bug ``` Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 GPUS := "2" PORT := "8001" launch_dp_ep_deepep_ll_no_em80: VLLM_USE_DEEP_GEMM_E8M0=0 VLLM_USE_DEEP_GEMM=1 VLLM_USE_DEEP_GEMM_MOE=1 chg run --gpu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: DeepEP LL Accuracy Issue with DeepGEMM E8M0 on B200 bug ### Your current environment B200 main ### 🐛 Describe the bug ``` Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8 GPUS := "2" PORT := "8001" launch_dp_ep_deepep_ll_no...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 1 VLLM_USE_DEEP_GEMM_MOE=1 chg run --gpus {{GPUS}} -- vllm serve {{MODEL_BLOCK}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --enforce-eager --all2all-backend deepep_low_latency launch_dp_ep_deepep_ll: VLLM_US...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31911](https://github.com/vllm-project/vllm/pull/31911) | mentioned | 0.6 | Add back missing DeepEP LL params | Add back missing DeepEP LL params Addresses #31844 introduced by a regression in f72a817. Before: ``` \|Tasks\|Version\| Filter \|n-shot\| Metric \| \|V |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
