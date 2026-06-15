# vllm-project/vllm#2235: Argument --pipeline-parallel-size/-pp: invalid int value: '8000:8000

| 字段 | 值 |
| --- | --- |
| Issue | [#2235](https://github.com/vllm-project/vllm/issues/2235) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Argument --pipeline-parallel-size/-pp: invalid int value: '8000:8000

### Issue 正文摘录

I'm experiencing an issue with the docker image when try to run it on runpod.io. I get the following error: `api_server.py: error: argument --pipeline-parallel-size/-pp: invalid int value: '8000:8000` I've follow the [docs](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) . I'm not sure what's causing this issue, but it's preventing me from using the vllm container. This is the runpod template configuration that i was using: ![Screenshot from 2023-12-21 14-28-54](https://github.com/vllm-project/vllm/assets/153531968/cd690e2c-afbc-4b0e-9583-1adbc260bfa6) Any help or guidance would be greatly appreciated. Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ipeline-parallel-size/-pp: invalid int value: '8000:8000 bug I'm experiencing an issue with the docker image when try to run it on runpod.io. I get the following error: `api_server.py: error: argument --pipeline-paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: preventing me from using the vllm container. This is the runpod template configuration that i was using: ![Screenshot from 2023-12-21 14-28-54](https://github.com/vllm-project/vllm/assets/153531968/cd690e2c-afbc-4b0e-95...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: int value: '8000:8000` I've follow the [docs](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html) . I'm not sure what's causing this issue, but it's preventing me from using the vllm container. This is th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
