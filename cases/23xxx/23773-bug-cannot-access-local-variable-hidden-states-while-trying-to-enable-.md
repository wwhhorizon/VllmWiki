# vllm-project/vllm#23773: [Bug]: `cannot access local variable 'hidden_states'` while trying to enable MTP for deepseek-r1

| 字段 | 值 |
| --- | --- |
| Issue | [#23773](https://github.com/vllm-project/vllm/issues/23773) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `cannot access local variable 'hidden_states'` while trying to enable MTP for deepseek-r1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempted to enable a [1p1d configuration of DeepSeek R1 with DP=8 with MTP](https://github.com/smarterclayton/ig-load/blob/3045bb2bee353db923e333c49fd0338eae392cdb/config/deploy_base_deepseek_r1_ep_pd.yaml#L81), but vLLM exited when the first request was dispatched: ``` (EngineCore_0 pid=463) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pid=463) self.run() (EngineCore_0 pid=463) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_0 pid=463) self._target(*self._args, **self._kwargs) (EngineCore_0 pid=463) File "/app/vllm/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_0 pid=463) raise e (EngineCore_0 pid=463) File "/app/vllm/vllm/v1/engine/core.py", line 701, in run_engine_core (EngineCore_0 pid=463) engine_core.run_busy_loop() (EngineCore_0 pid=463) File "/app/vllm/vllm/v1/engine/core.py", line 1044, in run_busy_loop (EngineCore_0 pid=463) executed = self._process_engine_step() (EngineCore_0 pid=463) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=463) File "/app/vllm/vllm/v1/engine/core.py", line 753, in _process_engine_step (EngineC...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: /deploy_base_deepseek_r1_ep_pd.yaml#L81), but vLLM exited when the first request was dispatched: ``` (EngineCore_0 pid=463) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 1p1d configuration of DeepSeek R1 with DP=8 with MTP](https://github.com/smarterclayton/ig-load/blob/3045bb2bee353db923e333c49fd0338eae392cdb/config/deploy_base_deepseek_r1_ep_pd.yaml#L81), but vLLM exited when the firs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _deepseek_r1_ep_pd.yaml#L81), but vLLM exited when the first request was dispatched: ``` (EngineCore_0 pid=463) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_0 pid=463) self....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lError: cannot access local variable 'hidden_states' where it is not associated with a value ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot livin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rent environment ### 🐛 Describe the bug Attempted to enable a [1p1d configuration of DeepSeek R1 with DP=8 with MTP](https://github.com/smarterclayton/ig-load/blob/3045bb2bee353db923e333c49fd0338eae392cdb/config/deploy_...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23776: Should have ROCm label: NO (0 matches) #23773: Should have ROCm label: NO (0 matches) #23768: Should have ROCm label: NO (0 matches) #23767: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
