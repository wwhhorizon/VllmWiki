# vllm-project/vllm#18228: [Doc]: Arguments missing from docs page

| 字段 | 值 |
| --- | --- |
| Issue | [#18228](https://github.com/vllm-project/vllm/issues/18228) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Arguments missing from docs page

### Issue 正文摘录

### 📚 The doc issue The following are arguments that are available by running `vllm serve --help` with vllm 0.8.4 and are not included in the [0.8.4 engine arguments docs](https://docs.vllm.ai/en/v0.8.4/serving/engine_args.html) page: ``` --allow-credentials --allowed-headers --allowed-methods --allowed-origins --api-key --chat-template --chat-template-content-format --config --disable-fastapi-docs --disable-frontend-multiprocessing --disable-uvicorn-access-log --enable-auto-tool-choice --enable-prompt-tokens-details --enable-request-id-headers --enable-server-load-tracking --enable-ssl-refresh --help --host --lora-modules --max-log-len --middleware --port --prompt-adapters --response-role --return-tokens-as-token-ids --root-path --ssl-ca-certs --ssl-cert-reqs --ssl-certfile --ssl-keyfile --tool-call-parser --tool-parser-plugin --uvicorn-log-level ``` It appears that the majority of these arguments are options that are created here: https://github.com/vllm-project/vllm/blob/0b34593017953051b3225b1483ce0f4670e3eb0e/vllm/entrypoints/openai/cli_args.py#L83 ### Suggest a potential alternative/fix Include the missing args in the engine args page. ### Before submitting a new issue... -...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hods --allowed-origins --api-key --chat-template --chat-template-content-format --config --disable-fastapi-docs --disable-frontend-multiprocessing --disable-uvicorn-access-log --enable-auto-tool-choice --enable-prompt-t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ss-log --enable-auto-tool-choice --enable-prompt-tokens-details --enable-request-id-headers --enable-server-load-tracking --enable-ssl-refresh --help --host --lora-modules --max-log-len --middleware --port --prompt-adap...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
