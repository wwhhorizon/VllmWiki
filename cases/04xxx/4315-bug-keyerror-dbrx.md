# vllm-project/vllm#4315: [Bug]: KeyError: 'dbrx'

| 字段 | 值 |
| --- | --- |
| Issue | [#4315](https://github.com/vllm-project/vllm/issues/4315) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KeyError: 'dbrx'

### Issue 正文摘录

### Your current environment See: https://github.com/vllm-project/vllm/issues/4312 ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/4312 for how ran. I don't really understand why this is happening. The hash is the same as another system that is running dbrx just fine. Good system that is running dbrx: ``` (h2ogpt) ubuntu@compute-permanent-node-212:~$ docker inspect --format='{{index .RepoDigests 0}}' d641d43b21fd vllm/vllm-openai@sha256:8fb3c30868764d169dc8837b153611815dbddbc831daafd8412b8f650fe111ae ``` Bad system that can't run dbrx: ``` ubuntu@compute-permanent-node-171:~/h2ogpt_ops$ docker inspect --format='{{index .RepoDigests 0}}' d641d43b21fd vllm/vllm-openai@sha256:8fb3c30868764d169dc8837b153611815dbddbc831daafd8412b8f650fe111ae ``` I guess dbrx model itself changed, so vLLM needs new transformers. ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 1155, in from_pretrained config_class = CONFIG_MAPPING[config_dict["model_type"]] File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 852, in __getitem__ raise KeyError(ke...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: dbrx: ``` (h2ogpt) ubuntu@compute-permanent-node-212:~$ docker inspect --format='{{index .RepoDigests 0}}' d641d43b21fd vllm/vllm-openai@sha256:8fb3c30868764d169dc8837b153611815dbddbc831daafd8412b8f650fe111ae ``` Bad sy...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: that is running dbrx: ``` (h2ogpt) ubuntu@compute-permanent-node-212:~$ docker inspect --format='{{index .RepoDigests 0}}' d641d43b21fd vllm/vllm-openai@sha256:8fb3c30868764d169dc8837b153611815dbddbc831daafd8412b8f650fe...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ration_auto.py", line 1155, in from_pretrained config_class = CONFIG_MAPPING[config_dict["model_type"]] File "/usr/local/lib/python3.10/dist-packages/transformers/models/auto/configuration_auto.py", line 852, in __getit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: KeyError: 'dbrx' bug;stale ### Your current environment See: https://github.com/vllm-project/vllm/issues/4312 ### 🐛 Describe the bug See https://github.com/vllm-project/vllm/issues/4312 for how ran. I don't reall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
