# vllm-project/vllm#4127: [Bug][Chunked prefill]: head size has to be power of two

| 字段 | 值 |
| --- | --- |
| Issue | [#4127](https://github.com/vllm-project/vllm/issues/4127) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][Chunked prefill]: head size has to be power of two

### Issue 正文摘录

### 🐛 Describe the bug The chunked prefill doesn't support head sizes that are not powers of two. For example, phi2 has head size of 80 (which is supported by flash attn, but the _flash_fwd triton kernel doesn't support it). Fix PR is coming. ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8) llm = LLM(model="microsoft/phi-2", enable_chunked_prefill=True) print(llm.generate("Hello, ", sampling_params)) ``` ``` Traceback (most recent call last): File "/workspaces/aici/py/vllm/test.py", line 7, in print(llm.generate("Hello, ", sampling_params)) File "/workspaces/aici/py/vllm/vllm/entrypoints/llm.py", line 190, in generate return self._run_engine(use_tqdm) File "/workspaces/aici/py/vllm/vllm/entrypoints/llm.py", line 218, in _run_engine step_outputs = self.llm_engine.step() File "/workspaces/aici/py/vllm/vllm/engine/llm_engine.py", line 735, in step output = self.model_executor.execute_model( File "/workspaces/aici/py/vllm/vllm/executor/gpu_executor.py", line 91, in execute_model output = self.driver_worker.execute_model( File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*...

## 现有链接修复摘要

#4128 [Bugfix][Kernel] allow non-power-of-two head sizes in prefix prefill

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: iton kernel doesn't support it). Fix PR is coming. ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0.8) llm = LLM(model="microsoft/phi-2", enable_chunked_prefill=True) print(l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mplingParams sampling_params = SamplingParams(temperature=0.8) llm = LLM(model="microsoft/phi-2", enable_chunked_prefill=True) print(llm.generate("Hello, ", sampling_params)) ``` ``` Traceback (most recent call last): F...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: as head size of 80 (which is supported by flash attn, but the _flash_fwd triton kernel doesn't support it). Fix PR is coming. ```python from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in execute_model output = self.model_runner.execute_model(seq_group_metadata_list, File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context return func(*args, **kwargs) Fi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4128](https://github.com/vllm-project/vllm/pull/4128) | closes_keyword | 0.95 | [Bugfix][Kernel] allow non-power-of-two head sizes in prefix prefill | FIX #4127 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </b> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
