# vllm-project/vllm#27043: [Bug]: FlashMLA: invalid configuration argument

| 字段 | 值 |
| --- | --- |
| Issue | [#27043](https://github.com/vllm-project/vllm/issues/27043) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;moe |
| 子分类 | precision |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashMLA: invalid configuration argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On B200 `vllm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 8 --enable-expert-parallel --port 9256` `vllm bench serve --model deepseek-ai/DeepSeek-V3.2-Exp --dataset-name random --host 127.0.0.1 --port 9256 --random-input-len 256 --random-output-len 256 --request-rate inf --num-prompts 1024` Will meet error ```bash CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA err...

## 现有链接修复摘要

#27271 [Attention] Fix DSv3.2 invalid configuration argument

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: pts 1024` Will meet error ```bash CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument CUDA error (/home/wentao/vllm-source/cmake-buil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: argument bug ### Your current environment ### 🐛 Describe the bug On B200 `vllm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 8 --enable-expert-parallel --port 9256` `vllm bench serve --model deepseek-ai/DeepSeek-V3.2-Exp --da...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: FlashMLA: invalid configuration argument bug ### Your current environment ### 🐛 Describe the bug On B200 `vllm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 8 --enable-expert-parallel --port 9256` `vllm bench serve --m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: bug On B200 `vllm serve deepseek-ai/DeepSeek-V3.2-Exp -dp 8 --enable-expert-parallel --port 9256` `vllm bench serve --model deepseek-ai/DeepSeek-V3.2-Exp --dataset-name random --host 127.0.0.1 --port 9256 --random-input...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t 127.0.0.1 --port 9256 --random-input-len 256 --random-output-len 256 --request-rate inf --num-prompts 1024` Will meet error ```bash CUDA error (/home/wentao/vllm-source/cmake-build-release/_deps/flashmla-src/csrc/smxx...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27271](https://github.com/vllm-project/vllm/pull/27271) | closes_keyword | 0.95 | [Attention] Fix DSv3.2 invalid configuration argument | Fixes #27043 by using `batch_size = num_tokens` instead of `batch_size = 1`. **NOTE**: running with `FULL_AND_PIECEWISE` cudagraphs still causes an IMA, this PR does not fix it. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
