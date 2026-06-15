# vllm-project/vllm#16205: [Installation]:  the --mount option requires BuildKit

| 字段 | 值 |
| --- | --- |
| Issue | [#16205](https://github.com/vllm-project/vllm/issues/16205) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]:  the --mount option requires BuildKit

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Step 8/90 : RUN --mount=type=cache,target=/root/.cache/uv python3 -m pip install uv the --mount option requires BuildKit. Refer to https://docs.docker.com/go/buildkit/ to learn how to build images with BuildKit enabled ### How you are installing vllm ```sh pip install -vvv vllm ``` I clone repo of vllm after that i run this command sudo docker build -t deepseek -f docker/Dockerfile . and got error at step 8/90 dont know why im getting im using azure VM of ubuntu 22.04 LTS to create docker image for installing deepseek in kubernetes for that i was create a docker image and also i try this also ``` DOCKER_BUILDKIT=1 docker build -t deepseek . failed to fetch metadata: fork/exec /home/azureuser/.docker/cli-plugins/docker-buildx: exec format error ERROR: BuildKit is enabled but the buildx component is missing or broken. Install the buildx component to build images with BuildKit: https://docs.docker.com/go/buildx/ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: the --mount option requires BuildKit installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Step 8/90 : RUN --mount=type=cache,target=/root/.cache/uv python
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: also ``` DOCKER_BUILDKIT=1 docker build -t deepseek . failed to fetch metadata: fork/exec /home/azureuser/.docker/cli-plugins/docker-buildx: exec format error ERROR: BuildKit is enabled but the buildx component is missi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: adata: fork/exec /home/azureuser/.docker/cli-plugins/docker-buildx: exec format error ERROR: BuildKit is enabled but the buildx component is missing or broken. Install the buildx component to build images with BuildKit:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: the --mount option requires BuildKit installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Step 8/90 : RUN --mount=type=cache,target=/root/.cache/uv python3 -m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
