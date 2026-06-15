# vllm-project/vllm#17639: [Bug]: Unable to run Qwen3 on Turing GPUs after upgrading to torch 2.7.0

| 字段 | 值 |
| --- | --- |
| Issue | [#17639](https://github.com/vllm-project/vllm/issues/17639) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Unable to run Qwen3 on Turing GPUs after upgrading to torch 2.7.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Turing GPUs (2080Ti) don't support bf16 and I have to use fp16. After upgrading torch to 2.7.0 I can no longer lanuch vllm when using dense Qwen3 or Qwen3Moe models. 1c2bc7ead019cdf5b04b2f1d07b00982352f85ef is the last working commit, 2c4f59afc3d50fda805c4ad94c9d9be168cded0b breaks it. Launch command: ``` vllm serve --dtype float16 --enable-chunked-prefill --enable-prefix-caching --gpu-memory-utilization 0.95 -tp 4 Qwen/Qwen3-30B-A3B --max-model-len 32768 --max-seq-len-to-capture 32768 --served-model-name Qwen3-30B-A3B --enable-reasoning --reasoning-parser qwen3 ``` The following lines in log looks like the culprit: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ...... in/home/sgsdxzy/micromamba/envs/vllm-dev/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py: 254:032o/home/sgsdxzy/micromamba/envs/vllm-dev/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/fused_moe.py:254:0: n: i c%aerror: 3lerror: = iarith.addizFailures have been detected while processing an MLIR pass pipeline eFailures have been detected while processing an MLIR pass p...

## 现有链接修复摘要

#7 Support beam search & parallel generation | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels | #68 Fix a bug in attention kernel | #4748 [CI] Nits for bad initialization of SeqGroup in testing

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ` The following lines in log looks like the culprit: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ...... in/home/sgsdxzy/micromamba/envs/vllm-dev/lib/python3.12/site-p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vironment ### 🐛 Describe the bug Turing GPUs (2080Ti) don't support bf16 and I have to use fp16. After upgrading torch to 2.7.0 I can no longer lanuch vllm when using dense Qwen3 or Qwen3Moe models. 1c2bc7ead019cdf5b04b...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ]: Unable to run Qwen3 on Turing GPUs after upgrading to torch 2.7.0 bug;stale ### Your current environment ### 🐛 Describe the bug Turing GPUs (2080Ti) don't support bf16 and I have to use fp16. After upgrading torch to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to run Qwen3 on Turing GPUs after upgrading to torch 2.7.0 bug;stale ### Your current environment ### 🐛 Describe the bug Turing GPUs (2080Ti) don't support bf16 and I have to use fp16. After upgrading torc...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | zled_shared<{vec = 1, perphase = 1, maxphase = 1, order = [0, 1]}>a :##7ttgsmem5. = "blocked<{sizeperthread = [4, 4], threadsperwarp = [2, 16], warpspercta = [4, 1], order = [1, 0… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | itt.splat%32 71}% = 65tt.splat: :tensor<%64 arg11xi i64:32 , i->#32 ttg tensor<->.slice<{dim = 1, parent = #blocked3}>64 >xtensor< i64->64x , 1tensor<#x64ttgix.32 1slice<{dim = |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | 2 55 ->%: 54 tensor< = tensor<1tt.addptr64x x64%1x52xi,i32 1, %, #53# blockedblocked:33 >>tensor< 64 x->%64 57xtensor< = !64arith.cmpittx .64sltptr<f16>x,, i #1%blocked, 513# |
| [#68](https://github.com/vllm-project/vllm/pull/68) | mentioned | 0.45 | Fix a bug in attention kernel | = tensor<.164slice<{dim = 0, parent = #blocked1}> : x>ii 3264 }, % #68:ttg = .tt.expand_dimstensor<slice<{dim = 0, parent = #blocked1}> 64>%x 34i {32%axis, 64 = # = 1ttgarith. |
| [#4748](https://github.com/vllm-project/vllm/pull/4748) | mentioned | 0.45 | [CI] Nits for bad initialization of SeqGroup in testing | 21 }x i%:3250 , = tensor<#tt.addptr64blocked x3%i>49 32, , %%#4748ttg = .tt.splat:slice<{dim = 0, parent = #blocked3}> >tensor<% 64arg14->x 1:tensor<x 1!ixtt3264. xptr<f16>- |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
