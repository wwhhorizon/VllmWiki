# vllm-project/vllm#23335: [Bug]: Missing tokens while streaming when using gpt-oss-20b

| 字段 | 值 |
| --- | --- |
| Issue | [#23335](https://github.com/vllm-project/vllm/issues/23335) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Missing tokens while streaming when using gpt-oss-20b

### Issue 正文摘录

### 🐛 Describe the bug I have served the gpt-oss model using vllm (0.10.0) ``` containers: - name: vllm-openai image: vllm/vllm-openai:gptoss imagePullPolicy: IfNotPresent env: - name: HF_TOKEN valueFrom: secretKeyRef: name: hf-token key: hf_token - name: VLLM_FLASH_ATTN_VERSION value: "3" command: - vllm - serve - /mnt/models/gpt-oss-20b - --host - "0.0.0.0" - --port - "8000" - --uvicorn-log-level - warning - --served-model-name - gpt-oss - --trust-remote-code - --gpu-memory-utilization - "0.9" - --enable-prefix-caching - --max-model-len - "8192" - --async-scheduling - --enable-log-requests ports: - containerPort: 8000 protocol: TCP volumeMounts: - mountPath: /mnt/models name: model-hostpath - mountPath: /dev/shm name: dshm resources: limits: nvidia.com/gpu: 1 requests: cpu: 8 nvidia.com/gpu: 1 ``` --- When sending a streaming requests using openai client, ``` completion = await openai.chat.completions.create( model=model, messages=messages, stream=True ) chunks = [] async for chunk in completion: chunks.append(chunk) content = chunk.choices[0].delta.content if content is not None: print(content, end="") ``` Model Response: ``` Good Afternoon Mr. Jaideep,’m calling from Tata Moto...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Missing tokens while streaming when using gpt-oss-20b bug;stale ### 🐛 Describe the bug I have served the gpt-oss model using vllm (0.10.0) ``` containers: - name: vllm-openai image: vllm/vllm-openai:gptoss imageP...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Missing tokens while streaming when using gpt-oss-20b bug;stale ### 🐛 Describe the bug I have served the gpt-oss model using vllm (0.10.0) ``` containers: - name: vllm-openai image: vllm/vllm-openai:gptoss imageP...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: name: hf-token key: hf_token - name: VLLM_FLASH_ATTN_VERSION value: "3" command: - vllm - serve - /mnt/models/gpt-oss-20b - --host - "0.0.0.0" - --port - "8000" - --uvicorn-log-level - warning - --serv
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: `). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
