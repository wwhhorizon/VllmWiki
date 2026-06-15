# vllm-project/vllm#23986: [Bug]: lmcache server points to wrong file in entrypoint

| 字段 | 值 |
| --- | --- |
| Issue | [#23986](https://github.com/vllm-project/vllm/issues/23986) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: lmcache server points to wrong file in entrypoint

### Issue 正文摘录

### Your current environment In this bug issue the environment information is not necessary. ### 🐛 Describe the bug The current implementation of lmcache-server in `deployment-cache-server.yaml` when: 1. using the `latest` tag assumes that the executable file is located in `/opt/venv/bin/lmcache_experimental_server` 2. using the version tag assumes that the executable file is located in `~/lmcache_experimental_server` ```yaml - name: "lmcache-server" image: "{{ required "Required value 'cacheserverSpec.repository' must be defined !" .Values.cacheserverSpec.repository }}:{{ required "Required value 'cacheserverSpec.tag' must be defined !" .Values.cacheserverSpec.tag }}" command: {{- if eq .Values.cacheserverSpec.tag "latest-nightly" }} - "/opt/venv/bin/lmcache_server" {{- else if eq .Values.cacheserverSpec.tag "latest" }} - "/opt/venv/bin/lmcache_experimental_server" {{- else }} - "lmcache_experimental_server" {{- end }} - "0.0.0.0" - "{{ .Values.cacheserverSpec.containerPort }}" {{- if .Values.cacheserverSpec.resources }} ``` But in fact, starting from `v0.3.0` of `lmcache/vllm-openai` the executable files are kept only in `/opt/venv/bin` and are named: 1. `lmcache_controller` 2....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e is located in `/opt/venv/bin/lmcache_experimental_server` 2. using the version tag assumes that the executable file is located in `~/lmcache_experimental_server` ```yaml - name: "lmcache-server" image: "{{ required "R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st-nightly" }} - "/opt/venv/bin/lmcache_server" {{- else if eq .Values.cacheserverSpec.tag "latest" }} - "/opt/venv/bin/lmcache_experimental_server" {{- else }} - "lmcache_experimental_server" {{- end }} - "0.0.0.0"
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nt bug ### Your current environment In this bug issue the environment information is not necessary. ### 🐛 Describe the bug The current implementation of lmcache-server in `deployment-cache-server.yaml` when: 1. using th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: f lmcache-server in `deployment-cache-server.yaml` when: 1. using the `latest` tag assumes that the executable file is located in `/opt/venv/bin/lmcache_experimental_server` 2. using the version tag assumes that the exe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
