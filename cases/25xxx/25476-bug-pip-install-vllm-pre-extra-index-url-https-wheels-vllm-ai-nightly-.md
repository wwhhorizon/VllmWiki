# vllm-project/vllm#25476: [Bug]: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly is broken again

| 字段 | 值 |
| --- | --- |
| Issue | [#25476](https://github.com/vllm-project/vllm/issues/25476) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly is broken again

### Issue 正文摘录

### Your current environment Run `pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` ### 🐛 Describe the bug The release `0.10.2` does not come from any branch in the upstream repo, see https://github.com/vllm-project/vllm/commit/e017120ed146cc3069d18428322d67881cb95e67 . This causes `git describe` to fail to find `0.10.2`. And it's finding another rc version instead. see https://buildkite.com/vllm/release/builds/8554/steps/canvas?sid=0199760b-38dd-46a3-9518-c71234514b04 for example, the nightly wheel's version is `0.10.2rc3.dev377+g231c2c63e.cu129` , and it will be shadowed by the official release 0.10.2 . To be more specific, `setuptools_scm` uses `git describe --dirty --tags --long --abbrev=40 --match "*[0-9]*"` to find the latest tag. And we should run it to make sure it gives the correct tag after release. NOTE: as a temporary fix, I pushed a fake tag https://github.com/vllm-project/vllm/tree/v0.11.0rc1 from the main branch. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly is broken again bug ### Your current environment Run `pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly` ### 🐛 Describ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ibe --dirty --tags --long --abbrev=40 --match "*[0-9]*"` to find the latest tag. And we should run it to make sure it gives the correct tag after release. NOTE: as a temporary fix, I pushed a fake tag https://github.com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
