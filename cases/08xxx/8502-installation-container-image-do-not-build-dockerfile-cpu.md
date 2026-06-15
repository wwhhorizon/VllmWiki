# vllm-project/vllm#8502: [Installation]: Container image do not build Dockerfile.cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#8502](https://github.com/vllm-project/vllm/issues/8502) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Container image do not build Dockerfile.cpu

### Issue 正文摘录

### Your current environment ```text $: podman -v podman version 5.2.2 ``` ### How you are installing vllm ```sh $: podman build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ... Error: building at STEP "RUN --mount=type=cache,target=/root/.cache/pip --mount=type=bind,src=requirements-build.txt,target=requirements-build.txt pip install --upgrade pip && pip install -r requirements-build.txt": resolving mountpoints for container "3a97f46183fa64e10c96f20f9a38a5ed46d2e9e7c4e7bbfbce6fa1adfdacd66e": invalid container path "requirements-build.txt", must be an absolute path ``` We can see that in the `Dockerfile.cpu` we are mounting the requirement-*.txt files https://github.com/vllm-project/vllm/blob/fc990f97958636ce25e4471acfd5651b096b0311/Dockerfile.cpu#L29 https://github.com/vllm-project/vllm/blob/fc990f97958636ce25e4471acfd5651b096b0311/Dockerfile.cpu#L51 https://github.com/vllm-project/vllm/blob/fc990f97958636ce25e4471acfd5651b096b0311/Dockerfile.cpu#L52 And while they are mounted, no absolute path is provided, leading to the error above. ## Solution proposal ```diff + COPY requirements-build.txt requirements-build.txt RUN --mount=type=cache,target=/root/.cache/pip \ - --mount=t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Container image do not build Dockerfile.cpu installation ### Your current environment ```text $: podman -v podman version 5.2.2 ``` ### How you are installing vllm ```sh $: podman build -f Dockerfile.cp
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 738 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ve path for target. I opened an issue on the buildah side to have more information https://github.com/containers/buildah/issues/5738 ### Before submitting a new issue... - [X] Make sure you already searched for relevant...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
