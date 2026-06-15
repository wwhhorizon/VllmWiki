# vllm-project/vllm#5867: IP Bind Error on v0.5.0.post1 

| 字段 | 值 |
| --- | --- |
| Issue | [#5867](https://github.com/vllm-project/vllm/issues/5867) |
| 状态 | closed |
| 标签 |  |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> IP Bind Error on v0.5.0.post1 

### Issue 正文摘录

Using the same forum.As I am encountering the same error on `0.5.0.post1` version. I am launching openai.api server using the following command and consistently seeing the IP-Bind error. It works on 0.4.2 version which is my current image. I am looking to upgrade to newer vllm version to access features/fixes that were failing on earlier version. ``` CMD="python -u -m vllm.entrypoints.openai.api_server \ -- host 0.0.0.0 \ --port $VLLM_PORT \ --model $launch_model \ --tensor-parallel-size $NUM_GPUS \ --download-dir /data" ``` Error: ``` ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 9000): address already in use ``` Appreciate any help with this. _Originally posted by @pchunduru10 in https://github.com/vllm-project/vllm/issues/1141#issuecomment-2192256236_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: sing the same forum.As I am encountering the same error on `0.5.0.post1` version. I am launching openai.api server using the following command and consistently seeing the IP-Bind error. It works on 0.4.2 version which i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: erver \ -- host 0.0.0.0 \ --port $VLLM_PORT \ --model $launch_model \ --tensor-parallel-size $NUM_GPUS \ --download-dir /data" ``` Error: ``` ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 9000)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
