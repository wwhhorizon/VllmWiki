# vllm-project/vllm#14115: [Bug]: ERROR 03-02 20:28:05 engine.py:400] Ovis has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#14115](https://github.com/vllm-project/vllm/issues/14115) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ERROR 03-02 20:28:05 engine.py:400] Ovis has no vLLM implementation and the Transformers implementation is not compatible with vLLM.

### Issue 正文摘录

### Your current environment https://modelscope.cn/models/AIDC-AI/Ovis2-34B https://modelscope.cn/models/AIDC-AI/Ovis2-16B the same problem. ![Image](https://github.com/user-attachments/assets/9dc347a3-5609-4233-b229-bd4ee1e473e9) root@node37:/disk1/Ovis2-16B# more docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: Ovis2-16B restart: always runtime: nvidia ports: - 8007:8000 volumes: - /disk1/:/models command: > --model /models/Ovis2-16B --trust_remote_code --tokenizer_mode="auto" --dtype=bfloat16 --max_num_seqs=128 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Ovis2-16B deploy: resources: reservations: devices: - driver: nvidia capabilities: [gpu] device_ids: [ "3" ] ipc: host networks: vllm: root@node37:/disk1/Ovis2-16B# root@node37:/disk1/Ovis2-16B# docker compose -f docker-compose.yml down root@node37:/disk1/Ovis2-16B# docker compose -f docker-compose.yml up -d [+] Running 2/2 ✔ Network ovis2-16b_default Created 0.1s ✔ Container Ovis2-16B Started 0.5s root@node37:/disk1/Ovis2-16B# docker logs -f Ovis2-16B INFO 03-02 20:27:49 __init__.py:207] Automatically detected plat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: dc347a3-5609-4233-b229-bd4ee1e473e9) root@node37:/disk1/Ovis2-16B# more docker-compose.yml version: '3.3' services: # vllm vllm-openai: image: vllm/vllm-openai:v0.7.3 container_name: Ovis2-16B restart: always runtime: n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: ion and the Transformers implementation is not compatible with vLLM. bug;stale ### Your current environment https://modelscope.cn/models/AIDC-AI/Ovis2-34B https://modelscope.cn/models/AIDC-AI/Ovis2-16B the same problem....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: vis2-16B --trust_remote_code --tokenizer_mode="auto" --dtype=bfloat16 --max_num_seqs=128 --tensor_parallel_size=1 --gpu-memory-utilization=0.9 --max-model-len=32768 --served-model-name=Ovis2-16B deploy: resources: reser...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: pace(host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: not compatible with vLLM. bug;stale ### Your current environment https://modelscope.cn/models/AIDC-AI/Ovis2-34B https://modelscope.cn/models/AIDC-AI/Ovis2-16B the same problem. ![Image](https://github.com/user-attachmen...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
