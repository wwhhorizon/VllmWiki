# vllm-project/vllm#23710: [Bug]: An error occurred during GPTQ quantization after updating the version and CUDA.

| 字段 | 值 |
| --- | --- |
| Issue | [#23710](https://github.com/vllm-project/vllm/issues/23710) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An error occurred during GPTQ quantization after updating the version and CUDA.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I encountered an error when loading Qwen3-235B-A22B-GPTQ-Int4 with the same command. ``` vllm serve qwen/Qwen3-235B-A22B-GPTQ-Int4 \ --tensor-parallel-size 8 \ --trust-remote-code \ --reasoning-parser qwen3 \ --enable-expert-parallel \ ``` error ``` Loading safetensors checkpoint shards: 0% Completed | 0/32 [00:00 (APIServer pid=2447410) sys.exit(main()) (APIServer pid=2447410) ^^^^^^ (APIServer pid=2447410) File "/home/odb/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/main.py", line 54, in main (APIServer pid=2447410) args.dispatch_function(args) (APIServer pid=2447410) File "/home/odb/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd (APIServer pid=2447410) uvloop.run(run_server(args)) (APIServer pid=2447410) File "/home/odb/miniconda3/envs/vllm/lib/python3.12/site-packages/uvloop/__init__.py", line 109, in run (APIServer pid=2447410) return __asyncio.run( (APIServer pid=2447410) ^^^^^^^^^^^^^^ (APIServer pid=2447410) File "/home/odb/miniconda3/envs/vllm/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=2447410) return runner.run(main) (A...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: An error occurred during GPTQ quantization after updating the version and CUDA. bug ### Your current environment ### 🐛 Describe the bug I encountered an error when loading Qwen3-235B-A22B-GPTQ-Int4 with the same...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rypoints/cli/main.py", line 54, in main (APIServer pid=2447410) args.dispatch_function(args) (APIServer pid=2447410) File "/home/odb/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/entrypoints/cli/serve.py", line...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: An error occurred during GPTQ quantization after updating the version and CUDA. bug ### Your current environment ### 🐛 Describe the bug I encountered an error when loading Qwen3-235B-A22B-GPTQ-Int4 with the same...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n error occurred during GPTQ quantization after updating the version and CUDA. bug ### Your current environment ### 🐛 Describe the bug I encountered an error when loading Qwen3-235B-A22B-GPTQ-Int4 with the same command....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment ### 🐛 Describe the bug I encountered an error when loading Qwen3-235B-A22B-GPTQ-Int4 with the same command. ``` vllm serve qwen/Qwen3-235B-A22B-GPTQ-Int4 \ --tensor-parallel-size 8 \ --trust-remote-code \ --rea...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23714: Should have ROCm label: NO (0 matches) #23710: Should have ROCm label: NO (0 matches) #23707: Should have ROCm label: NO (0 matches) #23702: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
