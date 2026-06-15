# vllm-project/vllm#12474: [Feature]: Better systemd security feature support

| 字段 | 值 |
| --- | --- |
| Issue | [#12474](https://github.com/vllm-project/vllm/issues/12474) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Better systemd security feature support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi maintainer, at the moment i want to run vllm on a system as a service with nginx in front of it and want to use some systemd security features to make the service run more secure. in these progress i found out that vllm is not compatible with the following settings: RestrictAddressFamilies=AF_INET AF_INET6 IPAddressDeny=any ProtectClock=true ### Alternatives these should work because all of these settings shouldnt be relevant for vllm to work.... ### Additional context FYI These is the config of the service file which it runs at the moment, i believe (but not tested) that i cant add more security features and it would still work ``` [Unit] Description=VLLM Service After=network.target [Service] Type=simple # if lower than WARNING than all the llm prompts are getting posted to the logs, so everything the user is asking the llm Environment="VLLM_LOGGING_LEVEL=WARNING" Environment="SIT=/networkpath/latest" Environment="CUDA_VISIBLE_DEVICES=3" ExecStart=/bin/bash -c '\ source ${SIT}/External/anaconda/conda/2024.02/BashSrc && \ conda activate /home/vllmrun/conda-env/vllm && \ vllm serve /home/vllmrun/MODELS/e5-mistral-7b-instruct \ --tensor-pa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ntrol Groups from modification ProtectControlGroups=true # prevents explicit Kernel module loading ProtectKernelModules=true # prevents Kernel tunables from being modified ProtectKernelTunables=true # With this setting...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OGGING_LEVEL=WARNING" Environment="SIT=/networkpath/latest" Environment="CUDA_VISIBLE_DEVICES=3" ExecStart=/bin/bash -c '\ source ${SIT}/External/anaconda/conda/2024.02/BashSrc && \ conda activate /home/vllmrun/conda-en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: relevant for vllm to work.... ### Additional context FYI These is the config of the service file which it runs at the moment, i believe (but not tested) that i cant add more security features and it would still work ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Better systemd security feature support feature request;stale ### 🚀 The feature, motivation and pitch Hi maintainer, at the moment i want to run vllm on a system as a service with nginx in front of it and wan...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nfig of the service file which it runs at the moment, i believe (but not tested) that i cant add more security features and it would still work ``` [Unit] Description=VLLM Service After=network.target [Service] Type=sim...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
