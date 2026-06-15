# vllm-project/vllm#42533: [Bug]: ngram_gpu speculative decoding can propose draft tokens past max_model_len budget

| 字段 | 值 |
| --- | --- |
| Issue | [#42533](https://github.com/vllm-project/vllm/issues/42533) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ngram_gpu speculative decoding can propose draft tokens past max_model_len budget

### Issue 正文摘录

### Environment Current `main` at commit `a8887c208f34c04c3b021cf3949ed6545d77bb01`. Tested on a Google Cloud A100 VM: - Driver: 580.126.20 - Python: 3.10.12 - vLLM: `0.20.2rc1.dev310+ga8887c208` from source/editable checkout - PyTorch: `2.11.0+cu130` - CUDA used to build PyTorch: 13.0 `python -m vllm.collect_env` excerpt: ```text ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 CUDA used to build PyTorch : 13.0 ============================== Python Environment ============================== Python version : 3.10.12 (main, Mar 3 2026, 11:56:32) [GCC 11.4.0] Python platform : Linux-6.8.0-1053-gcp-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB Nvidia driver version : 580.126.20 cuDNN version : 9.13.0 libraries present ============================== vLLM Info ============================== vLLM Version : 0.20...

## 现有链接修复摘要

#43049 fix: cap ngram gpu drafts by max model length

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ` from source/editable checkout - PyTorch: `2.11.0+cu130` - CUDA used to build PyTorch: 13.0 `python -m vllm.collect_env` excerpt: ```text ============================== System Info ============================== OS : U...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: it `a8887c208f34c04c3b021cf3949ed6545d77bb01`. Tested on a Google Cloud A100 VM: - Driver: 580.126.20 - Python: 3.10.12 - vLLM: `0.20.2rc1.dev310+ga8887c208` from source/editable checkout - PyTorch: `2.11.0+cu130` - CUD...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ngram_gpu speculative decoding can propose draft tokens past max_model_len budget ### Environment Current `main` at commit `a8887c208f34c04c3b021cf3949ed6545d77bb01`. Tested on a Google Cloud A100 VM: - Driver: 5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: ngram_gpu speculative decoding can propose draft tokens past max_model_len budget ### Environment Current `main` at commit `a8887c208f34c04c3b021cf3949ed6545d77bb01`. Tested on a Google Cloud A100 VM: - Driver: 5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t Current `main` at commit `a8887c208f34c04c3b021cf3949ed6545d77bb01`. Tested on a Google Cloud A100 VM: - Driver: 580.126.20 - Python: 3.10.12 - vLLM: `0.20.2rc1.dev310+ga8887c208` from source/editable checkout - PyTor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43049](https://github.com/vllm-project/vllm/pull/43049) | closes_keyword | 0.95 | fix: cap ngram gpu drafts by max model length | fix direction described in #42533. Duplicate-work check: before opening this PR, I verified that #42533 was open and unassigned, had no linked branches or pull requests, and tha |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
