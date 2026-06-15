# vllm-project/vllm#31404: [Bug]: MM cache AssertionError crashes engine, causes request aborts

| 字段 | 值 |
| --- | --- |
| Issue | [#31404](https://github.com/vllm-project/vllm/issues/31404) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MM cache AssertionError crashes engine, causes request aborts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are serving `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` on vLLM, but after some time an error occurs in the multimodal cache, and after that all requests are aborted until we restart the server. ``` ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m Exception in thread Thread-5 (process_input_sockets): ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m Traceback (most recent call last): ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m File "/usr/lib/python3.12/threading.py", line 1073, in _bootstrap_inner ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m self.run() ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m File "/usr/lib/python3.12/threading.py", line 1010, in run ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m self._target(*self._args, **self._kwargs) ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m File "/mnt/external-hard2/projects/serving/deploy/vllm/.venv/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1053, in process_input_sockets ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m request = self.preprocess_add_request(request) ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ESC[0;36m(EngineCore_DP0 pid=52470)ESC[0;0m File...

## 现有链接修复摘要

#34749 fix: replace fatal assertions with MultiModalCacheMissError in MM cache

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug We are serving `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` on vLLM, but after some time an error occurs in the multimodal cache, and after that all requests are aborted until...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: _tokens=2115, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=False, spaces_between _special_tokens=True, truncate_prompt_tokens=None, structured_outputs=None, extra_args=None), lora_request: None...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### 🐛 Describe the bug We are serving `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` on vLLM, but after some time an error occurs in the multimodal cache, and after that all requests are aborted until we restart the server. ``` E...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MM cache AssertionError crashes engine, causes request aborts bug ### Your current environment ### 🐛 Describe the bug We are serving `Qwen/Qwen3-VL-30B-A3B-Instruct-FP8` on vLLM, but after some time an error occu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34749](https://github.com/vllm-project/vllm/pull/34749) | closes_keyword | 0.95 | fix: replace fatal assertions with MultiModalCacheMissError in MM cache | Fix #31404 The multimodal (MM) processor cache can crash the engine's `process_input_sockets` thread with an `AssertionError` when an item expected to be cached has been evicted f |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
