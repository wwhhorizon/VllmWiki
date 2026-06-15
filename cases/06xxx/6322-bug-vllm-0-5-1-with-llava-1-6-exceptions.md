# vllm-project/vllm#6322: [Bug]: VLLM 0.5.1 with LLaVA 1.6 exceptions

| 字段 | 值 |
| --- | --- |
| Issue | [#6322](https://github.com/vllm-project/vllm/issues/6322) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;sampling |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.5.1 with LLaVA 1.6 exceptions

### Issue 正文摘录

### Your current environment See https://github.com/vllm-project/vllm/issues/6176 ### 🐛 Describe the bug I have lots of image, where the service throws exception and after that must be restarted, because it stucks in exception mode, even for images, that worked before. Example image below. ``` curl 'https://ai1.dev.init/multimodal-llava/v1/chat/completions' -k -H 'Content-Type: application/json' -d @- , error_callback= >) handle: , error_callback= >)> Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 43, in _log_task_completion return_value = task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 595, in run_engine_loop result = task.result() File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 540, in engine_step request_outputs = await self.engine.step_async(virtual_engine) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 241, in step_async output = await self.model_executor.execute_model_async( File "/usr/local/lib/python3.10/dist-packages/vllm/executor/distributed_gpu_executor.py", line 173, in exe...

## 现有链接修复摘要

#6339 [bug fix] Fix llava next feature size calculation.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: that worked before. Example image below. ``` curl 'https://ai1.dev.init/multimodal-llava/v1/chat/completions' -k -H 'Content-Type: application/json' -d @- , error_callback= >) handle: , error_callback= >)> Traceback (mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 38 - "POST /v1/chat/completions HTTP/1.0" 400 Bad Request ``` Config of Docker image: ``` services: vllm-llava: image: vllm/vllm-openai:v0.5.1 container_name: vllm-llava ipc: host deploy: resources: reservations: device...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: -packages/vllm/engine/async_llm_engine.py", line 540, in engine_step request_outputs = await self.engine.step_async(virtual_engine) File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 24...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6339](https://github.com/vllm-project/vllm/pull/6339) | closes_keyword | 0.95 | [bug fix] Fix llava next feature size calculation. | Closes #6322 cc @ywang96 @DarkLight1337 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
