# vllm-project/vllm#6224: [Bug]: Error while running inference with LLava 1.6 in v0.5.1 

| 字段 | 值 |
| --- | --- |
| Issue | [#6224](https://github.com/vllm-project/vllm/issues/6224) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while running inference with LLava 1.6 in v0.5.1 

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-5.15.0-1049-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A10G GPU 1: NVIDIA A10G GPU 2: NVIDIA A10G GPU 3: NVIDIA A10G Nvidia driver version: 535.104.12 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so...

## 现有链接修复摘要

#6364 [Misc][Bugfix] Update transformers for tokenizer issue

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rrent environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: .5.1 bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec rstack overflow: Mit...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6364](https://github.com/vllm-project/vllm/pull/6364) | closes_keyword | 0.95 | [Misc][Bugfix] Update transformers for tokenizer issue | CLOSE #6224 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
