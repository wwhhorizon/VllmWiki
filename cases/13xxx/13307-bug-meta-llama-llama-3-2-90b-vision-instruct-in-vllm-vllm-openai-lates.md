# vllm-project/vllm#13307: [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct in vllm/vllm-openai:latest

| 字段 | 值 |
| --- | --- |
| Issue | [#13307](https://github.com/vllm-project/vllm/issues/13307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct in vllm/vllm-openai:latest

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` version: '3.8' services: vllm-vllama-api: image: vllm/vllm-openai:latest environment: - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN} volumes: - ./vllm-llama3.2:/root/.cache/huggingface command: [ "--model", "meta-llama/Llama-3.2-90B-Vision-Instruct", "--enforce-eager", "--tensor-parallel-size", "2", "--max-num-seqs", "16", "--trust-remote-code" ] deploy: resources: reservations: devices: - driver: nvidia capabilities: [ gpu ] device_ids: [ '5', '6' ] ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 989, in from_pretrained config_class = CONFIG_MAPPING[config_dict["model_type"]] File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 691, in __getitem__ raise KeyError(key) KeyError: 'mllama' During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: meta-llama/Llama-3.2-90B-Vision-Instruct in vllm/vllm-openai:latest bug;stale ### Your current environment ### 🐛 Describe the bug ``` version: '3.8' services: vllm-vllama-api: image: vllm/vllm-openai:latest en
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t bug;stale ### Your current environment ### 🐛 Describe the bug ``` version: '3.8' services: vllm-vllama-api: image: vllm/vllm-openai:latest environment: - HUGGING_FACE_HUB_TOKEN=${HF_TOKEN} volumes: - ./vllm-llama3.2:/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nfiguration_auto.py", line 989, in from_pretrained config_class = CONFIG_MAPPING[config_dict["model_type"]] File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 691, in __g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to load has model type `mllama` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date. Is the reason that th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: meta-llama/Llama-3.2-90B-Vision-Instruct in vllm/vllm-openai:latest bug;stale ### Your current environment ### 🐛 Describe the bug ``` version: '3.8' services: vllm-vllama-api: image: vllm/vllm-openai:latest environment:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
