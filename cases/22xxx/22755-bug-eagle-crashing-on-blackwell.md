# vllm-project/vllm#22755: [Bug]: EAGLE crashing on Blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#22755](https://github.com/vllm-project/vllm/issues/22755) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE crashing on Blackwell

### Issue 正文摘录

### Your current environment Followed standard installation steps for 0.10.0, also observed on latest main. ``` export VLLM_VERSION=0.10.0 export CUDA_VERSION=126 uv pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu126-cp38-abi3-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu${CUDA_VERSION} --index-strategy unsafe-best-match ``` ### 🐛 Describe the bug Crashes on first request sent to the server when EAGLE is enabled with CUDA graphs. Works fine for enforce-eager. To run: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 1 --speculative-config '{"num_speculative_tokens": 1, "method": "eagle", "model": "yuhuili/EAGLE-LLaMA3.1-Instruct-8B"}' --trust-remote-code --no-enable-prefix-caching ``` Also tried with `VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_FLASH_ATTN_VERSION=2`, no change. Output: ```ERROR 08-12 18:22:15 [core.py:634] EngineCore encountered a fatal error. ERROR 08-12 18:22:15 [core.py:634] Traceback (most recent call last): ERROR 08-12 18:22:15 [core.py:634] File "/root/eagle/vllm_centml_fork/.vllm_env/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 625, in run...

## 现有链接修复摘要

#22684 [V1][Spec Decode] Fix MTP bugs and enable MLA support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rashing on Blackwell bug ### Your current environment Followed standard installation steps for 0.10.0, also observed on latest main. ``` export VLLM_VERSION=0.10.0 export CUDA_VERSION=126 uv pip install https://github.c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ategy unsafe-best-match ``` ### 🐛 Describe the bug Crashes on first request sent to the server when EAGLE is enabled with CUDA graphs. Works fine for enforce-eager. To run: ``` vllm serve meta-llama/Llama-3.1-8B-Instruc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: EAGLE crashing on Blackwell bug ### Your current environment Followed standard installation steps for 0.10.0, also observed on latest main. ``` export VLLM_VERSION=0.10.0 export CUDA_VERSION=126 uv pip install ht...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CUDA graphs. Works fine for enforce-eager. To run: ``` vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 1 --speculative-config '{"num_speculative_tokens": 1, "method": "eagle", "model": "yuhuili/EAGLE-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mote-code --no-enable-prefix-caching ``` Also tried with `VLLM_ATTENTION_BACKEND=FLASH_ATTN VLLM_FLASH_ATTN_VERSION=2`, no change. Output: ```ERROR 08-12 18:22:15 [core.py:634] EngineCore encountered a fatal error. ERRO...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22684](https://github.com/vllm-project/vllm/pull/22684) | closes_keyword | 0.95 | [V1][Spec Decode] Fix MTP bugs and enable MLA support | fixed by this PR (#22755) ## Review Notes I wish to guide reviewers towards some specific topics of discussion related to the design decisions made in this implementation: ### E |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
