# vllm-project/vllm#5213: [Bug]: prompt_logprobs=0 raises AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#5213](https://github.com/vllm-project/vllm/issues/5213) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: prompt_logprobs=0 raises AssertionError

### Issue 正文摘录

### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.35 Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] (64-bit runtime) ... ### 🐛 Describe the bug With vllm==0.4.3, `prompt_logprobs=0` raises AssertionError on the shape of (pruned) logits. ```python import vllm llm = vllm.LLM("facebook/opt-125m") llm.generate(["Hello, my name is"], vllm.SamplingParams(prompt_logprobs=0)) ``` raises ``` Traceback (most recent call last): File "/home/kataoka/venv/lib/python3.10/site-packages/IPython/core/interactiveshell.py", line 3553, in run_code exec(code_obj, self.user_global_ns, self.user_ns) File "/tmp/ipykernel_2972011/3028385135.py", line 1, in llm.generate(["Hello, my name is"], vllm.SamplingParams(prompt_logprobs=0)) File "/home/kataoka/venv/lib/python3.10/site-packages/vllm/utils.py", line 672, in inner return fn(*args, **kwargs) File "/home/kataoka/venv/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line...

## 现有链接修复摘要

#5217 [Bugfix] Support `prompt_logprobs==0`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: gprobs=0 raises AssertionError bug ### Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: Your current environment PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: packages/vllm/engine/llm_engine.py", line 772, in step output = self.model_executor.execute_model( File "/home/kataoka/venv/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 91, in execute_model output =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nnot be used with `echo=True` in OpenAI-compatible API: ```python import requests requests.post("http://localhost:8000/v1/completions", json=dict( model="facebook/opt-125m", prompt="Hello, my name is", max_tokens=10, lo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5217](https://github.com/vllm-project/vllm/pull/5217) | closes_keyword | 0.95 | [Bugfix] Support `prompt_logprobs==0` | FIX #5213 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
