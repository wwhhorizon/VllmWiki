# vllm-project/vllm#26110: [RFC]: CI metrics dashboard improvements

| 字段 | 值 |
| --- | --- |
| Issue | [#26110](https://github.com/vllm-project/vllm/issues/26110) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: CI metrics dashboard improvements

### Issue 正文摘录

### Motivation. Our CI metrics are currently fragmented and we utilize multiple dashboards. We also lack several key metrics such as % of force merges or PR cycle times. We currently have [a dashboard ](https://app.hex.tech/533fe68e-dcd8-4a52-a101-aefba762f581/app/vLLM-CI-030kdEgDv6lSlh1UPYOkWP/latest)tracking some important CI metrics as well as buildkite UI. We seek to improve upon that by integrating vLLM with the comprehensive set of features offered by [pytorch HUD](https://hud.pytorch.org) and offer a single unified dashboard. We will also use this opportunity to review and enhance all the different metrics we are tracking. ### Proposed Change. After integration with Pytorch HUD, we will implement the following metrics: ### Reporting defaults - Time window: last 7 days - Aggregations shown by default: 90th percentile, mean, and maximum - Segmentation: by repository, pipeline, step, agent queue (agent type), team, pull request size, and day of week ### Definitions - On red: any required check is failing at the time of merge. - Impatience: merged while required checks were still pending. - Time to green: from the first CI job start to the last required job success. Exclude can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [RFC]: CI metrics dashboard improvements RFC;stale ### Motivation. Our CI metrics are currently fragmented and we utilize multiple dashboards. We also lack several key metrics such as % of force merges or PR cycle times...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: CI metrics dashboard improvements RFC;stale ### Motivation. Our CI metrics are currently fragmented and we utilize multiple dashboards. We also lack several key metrics such as % of force merges or PR cycle times...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: y a non-author. Include Codeowners bypass count if applicable. - Merge block reasons - CI red - CI green but pending review ### Buildkite pipeline and job metrics **Primary** - **End-to-end CI duration**: wall time from...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 33fe68e-dcd8-4a52-a101-aefba762f581/app/vLLM-CI-030kdEgDv6lSlh1UPYOkWP/latest)tracking some important CI metrics as well as buildkite UI. We seek to improve upon that by integrating vLLM with the comprehensive set of fe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
