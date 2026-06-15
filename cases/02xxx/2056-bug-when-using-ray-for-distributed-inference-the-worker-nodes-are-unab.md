# vllm-project/vllm#2056: Bug: When using Ray for distributed inference, the worker nodes are unable to pull models from ModelScope.

| 字段 | 值 |
| --- | --- |
| Issue | [#2056](https://github.com/vllm-project/vllm/issues/2056) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug: When using Ray for distributed inference, the worker nodes are unable to pull models from ModelScope.

### Issue 正文摘录

```shell VLLM_USE_MODELSCOPE=True python api_server.py --model=qwen/Qwen-14B-Chat --trust-remote-code --tensor-parallel-size 4 ``` I executed the above command. It's anticipated that each participating node in this distributed inference task will download the model to its local path. However, at present, only the head node has accomplished this. And the error like: `No such file or directory: '/home/ray/.cache/modelscope/hub/qwen/Qwen-14B-Chat/-home-ray-.cache-modelscope-hub-qwen-Qwen-14B-Chat.lock'` The code to download models from ModelScope does not seem to have been submitted to the Ray cluster.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: using Ray for distributed inference, the worker nodes are unable to pull models from ModelScope. ```shell VLLM_USE_MODELSCOPE=True python api_server.py --model=qwen/Qwen-14B-Chat --trust-remote-code --tensor-parallel-si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: code --tensor-parallel-size 4 ``` I executed the above command. It's anticipated that each participating node in this distributed inference task will download the model to its local path. However, at present, only the h...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
