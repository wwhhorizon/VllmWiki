# vllm-project/vllm#9623: [Bug]: Incompatible shape in block table when running Phi-3.5-mini-instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#9623](https://github.com/vllm-project/vllm/issues/9623) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cache |
| 症状 | build_error;crash |
| 根因提示 | memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incompatible shape in block table when running Phi-3.5-mini-instruct

### Issue 正文摘录

### Your current environment I am using the docker sudo docker run -d --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --trust-remote-code \ --gpu-memory-utilization 1 \ --max-model-len 32000 \ --enable-auto-tool-choice \ --tool-call-parser llama3_json \ --model microsoft/Phi-3.5-mini-instruct ### Model Input Dumps _No response_ ### 🐛 Describe the bug ERROR 10-23 09:23:34 engine.py:158] ValueError('could not broadcast input array from shape (581,) into shape (512,)') ERROR 10-23 09:23:34 engine.py:158] Traceback (most recent call last): ERROR 10-23 09:23:34 engine.py:158] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 156, in start ERROR 10-23 09:23:34 engine.py:158] self.run_engine_loop() ERROR 10-23 09:23:34 engine.py:158] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 219, in run_engine_loop ERROR 10-23 09:23:34 engine.py:158] request_outputs = self.engine_step() ERROR 10-23 09:23:34 engine.py:158] ^^^^^^^^^^^^^^^^^^ ERROR 10-23 09:23:34 engine.py:158] File "/usr/local/lib/python3.12/dist-packages/vllm/engi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 3.5-mini-instruct bug;stale ### Your current environment I am using the docker sudo docker run -d --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-op...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Incompatible shape in block table when running Phi-3.5-mini-instruct bug;stale ### Your current environment I am using the docker sudo docker run -d --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: er sudo docker run -d --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest \ --trust-remote-code \ --gpu-memory-utilization 1 \ --max-model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Incompatible shape in block table when running Phi-3.5-mini-instruct bug;stale ### Your current environment I am using the docker sudo docker run -d --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/hug...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e.py:158] File "/usr/local/lib/python3.12/dist-packages/vllm/attention/backends/utils.py", line 215, in build ERROR 10-23 09:23:34 engine.py:158] input_block_tables[i, :len(block_table)] = block_table ERROR 10-23 09:23:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
