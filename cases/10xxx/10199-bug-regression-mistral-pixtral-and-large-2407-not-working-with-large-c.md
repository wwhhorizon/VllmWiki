# vllm-project/vllm#10199: [Bug/Regression]: Mistral Pixtral and Large 2407 not working with large context in 0.6.3post1 (0.6.1post2 works fine)

| 字段 | 值 |
| --- | --- |
| Issue | [#10199](https://github.com/vllm-project/vllm/issues/10199) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug/Regression]: Mistral Pixtral and Large 2407 not working with large context in 0.6.3post1 (0.6.1post2 works fine)

### Issue 正文摘录

### Your current environment vllm-tgi: container_name: vllm-tgi image: vllm/vllm-openai:v0.6.3.post1 restart: always shm_size: "16gb" command: "--model /model --served-model-name mistral-large-123b --tensor-parallel-size 4 --port 8081 --api-key kitch_vllm --tokenizer_mode mistral --load_format safetensors --config_format mistral" ports: - "8081:8081" environment: - HTTP_PROXY= - HTTPS_PROXY= - http_proxy= - https_proxy= volumes: - ${PATH_MODEL_GENERATION}:/model deploy: resources: reservations: devices: - driver: nvidia device_ids: [ '0', '1', '2', '3' ] capabilities: [ gpu ] ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tested Mistral-Large-2407 with v0.6.3post1 and got really strange results when using a long context. With small context it worked well. With v0.6.1post2 everything works as expected. The output looks like this: ```</textlichkeitsertei n Aufgereign Abbetzeilen: OFFENDELETZuswelternationalis von dem Aufgültigkeitschiff OFFENDE OFFENDEUTBereichter: OFFENDE ENDE OFFENGebsowie die Aufgaben: OFFENDETAUmeter: OFFENFOR OFFEN OFFENDESTELLIPS- Stätzugennt- Stellungskomitestellung durch den Aufgeler: 22 • räus- </ AufgStell OFFENG </ </contextsowie geordnungsf...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ai:v0.6.3.post1 restart: always shm_size: "16gb" command: "--model /model --served-model-name mistral-large-123b --tensor-parallel-size 4 --port 8081 --api-key kitch_vllm --tokenizer_mode mistral --load_format safetenso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .6.3post1 and got really strange results when using a long context. With small context it worked well. With v0.6.1post2 everything works as expected. The output looks like this: ```</textlichkeitsertei n Aufgereign Abbe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug/Regression]: Mistral Pixtral and Large 2407 not working with large context in 0.6.3post1 (0.6.1post2 works fine) bug ### Your current environment vllm-tgi: container_name: vllm-tgi image: vllm/vllm-openai:v0.6

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
