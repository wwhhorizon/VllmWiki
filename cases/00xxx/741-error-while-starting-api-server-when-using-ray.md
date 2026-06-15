# vllm-project/vllm#741: Error while starting API server when using Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#741](https://github.com/vllm-project/vllm/issues/741) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error while starting API server when using Ray

### Issue 正文摘录

I am installing the vllm using ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y WORKDIR /workspace RUN pip install vllm EXPOSE 8097 ``` start vllm server using `docker run --gpus all --shm-size=20g -p 8097:8097 -it --rm --name vllm vllm_docker python3 -m vllm.entrypoints.api_server --port 8097 --host 0.0.0.0 --trust-remote-code --tensor-parallel-size 8` ``` The last 20 lines of /tmp/ray/session_2023-08-11_20-00-52_804243_1/logs/dashboard.log (it contains the error message from the dashboard): from ray.util.state.common import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/__init__.py", line 1, in from ray.util.state.api import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/api.py", line 17, in from ray.util.state.common import ( File "/usr/local/lib/python3.8/dist-packages/ray/util/state/common.py", line 420, in class ActorState(StateSchema): File "pydantic/dataclasses.py", line 224, in pydantic.dataclasses.dataclass.wrap File "pydantic/dataclasses.py", line 336, in pydantic.dataclasses._add_pydantic_validation_attributes File "pydantic/dataclasses.py", line 391, in pydantic.dataclasses.create_pydantic_model_from_dataclass File "py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Error while starting API server when using Ray I am installing the vllm using ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y WORKDIR /workspace RUN pip install vllm EXPOSE 8097 ``` start vllm serve...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: antic/dataclasses.py", line 391, in pydantic.dataclasses.create_pydantic_model_from_dataclass File "pydantic/main.py", line 1026, in pydantic.main.create_model File "pydantic/main.py", line 198, in pydantic.main.ModelMe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
