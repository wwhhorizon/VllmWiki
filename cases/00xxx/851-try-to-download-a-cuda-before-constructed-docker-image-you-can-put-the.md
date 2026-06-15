# vllm-project/vllm#851: try to download a cuda before constructed docker image, you can put the step of download cuda in the dockerfile.

| 字段 | 值 |
| --- | --- |
| Issue | [#851](https://github.com/vllm-project/vllm/issues/851) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> try to download a cuda before constructed docker image, you can put the step of download cuda in the dockerfile.

### Issue 正文摘录

try to download a cuda before constructed docker image, you can put the step of download cuda in the dockerfile. such as : RUN apt-get update && \ apt-get install -y --no-install-recommends \ wget && \ rm -rf /var/lib/apt/lists/* RUN wget https://developer.download.nvidia.com/compute/cuda/11.0.3/local_installers/cuda_11.0.3_450.51.06_linux.run && \ chmod +x cuda_11.0.3_450.51.06_linux.run && \ ./cuda_11.0.3_450.51.06_linux.run --silent --toolkit --override && \ rm cuda_11.0.3_450.51.06_linux.run _Originally posted by @Shiyubo980980 in https://github.com/vllm-project/vllm/issues/807#issuecomment-1691102110_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: try to download a cuda before constructed docker image, you can put the step of download cuda in the dockerfile. try to download a cuda before constructed docker image, you can put the step of download cuda in the docke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: try to download a cuda before constructed docker image, you can put the step of download cuda in the dockerfile. try to download a cuda before constructed docker image, you can put the step of download cuda in the docke...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
