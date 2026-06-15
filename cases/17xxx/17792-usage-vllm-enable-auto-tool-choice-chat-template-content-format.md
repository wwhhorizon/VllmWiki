# vllm-project/vllm#17792: [Usage]: 自己部署vllm，无法调用工具，需要开启--enable-auto-tool-choice，开启后提示要配置--chat-template-content-format，最后报错

| 字段 | 值 |
| --- | --- |
| Issue | [#17792](https://github.com/vllm-project/vllm/issues/17792) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | crash;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: 自己部署vllm，无法调用工具，需要开启--enable-auto-tool-choice，开启后提示要配置--chat-template-content-format，最后报错

### Issue 正文摘录

### Your current environment ```text 1. 第一次部署 `sudo docker run --runtime nvidia --gpus all \ -v /media/modules:/root/model \ -p 8000:8000 \ --ipc=host \ --name t1 \ vllm/vllm-openai:latest \ --model /root/model/glm-edge-1.5b-chat \ --max-model-len 8000 --dtype auto \ --tensor-parallel-size 1 2. 该部署报错如下 `Error code: 400 - {'object': 'error', 'message': '"auto" tool choice requires --enable-auto-tool-choice and --tool-call-parser to be set', 'type': 'BadRequestError', 'param': None, 'code': 400} ` 服务器报错： `INFO 05-07 04:42:17 [chat_utils.py:396] Detected the chat template content format to be 'string'. You can set `--chat-template-content-format` to override this. ERROR 05-07 04:42:17 [serving_chat.py:198] Error in preprocessing prompt inputs ERROR 05-07 04:42:17 [serving_chat.py:198] Traceback (most recent call last): ERROR 05-07 04:42:17 [serving_chat.py:198] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/serving_chat.py", line 181, in create_chat_completion ERROR 05-07 04:42:17 [serving_chat.py:198] ) = await self._preprocess_chat( ERROR 05-07 04:42:17 [serving_chat.py:198] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-07 04:42:17 [serving_chat.py:198] File "/usr/lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t，最后报错 usage;stale ### Your current environment ```text 1. 第一次部署 `sudo docker run --runtime nvidia --gpus all \ -v /media/modules:/root/model \ -p 8000:8000 \ --ipc=host \ --name t1 \ vllm/vllm-openai:latest \ --model /...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm，无法调用工具，需要开启--enable-auto-tool-choice，开启后提示要配置--chat-template-content-format，最后报错 usage;stale ### Your current environment ```text 1. 第一次部署 `sudo docker run --runtime nvidia --gpus all \ -v /media/modules:/root/model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nable-auto-tool-choice，开启后提示要配置--chat-template-content-format，最后报错 usage;stale ### Your current environment ```text 1. 第一次部署 `sudo docker run --runtime nvidia --gpus all \ -v /media/modules:/root/model \ -p 8000:8000 \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: -p 8000:8000 \ --ipc=host \ --name t1 \ vllm/vllm-openai:latest \ --model /root/model/glm-edge-1.5b-chat \ --max-model-len 8000 --dtype auto \ --tensor-parallel-size 1 2. 该部署报错如下 `Error code: 400 - {'object': 'error', '...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: --model /root/model/glm-edge-1.5b-chat \ --max-model-len 8000 --dtype auto \ --tensor-parallel-size 1 2. 该部署报错如下 `Error code: 400 - {'object': 'error', 'message': '"auto" tool choice requires --enable-auto-tool-choice a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
