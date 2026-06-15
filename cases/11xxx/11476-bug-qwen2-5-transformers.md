# vllm-project/vllm#11476: [Bug]: Qwen2.5推理长上下文导致回复不完整，使用transformers库可以得到完整结果

| 字段 | 值 |
| --- | --- |
| Issue | [#11476](https://github.com/vllm-project/vllm/issues/11476) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;quantization;sampling |
| 症状 | nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5推理长上下文导致回复不完整，使用transformers库可以得到完整结果

### Issue 正文摘录

### Your current environment ### Model Input Dumps ``` prompt= f''' 以下内容摘自文档广东省实施《水文监测数据通信规约》细则.docx，文档编号1：——分片——\n\n附录I\n（资料性附录）报文示例\n\nI.1遥测站定时报\n\nI.1.1雨量站小时报，功能码34H\n上行：\n7E7E1000123456781234340038020001140612020000F1F1001234567850F0F01406120200F460000000000000000000000000261900000020190000001A1900000038121290034383\n协议解析：\n \n|报文|编码名称|编码说明|\n|7E7E|帧头|2字节HEX编码|\n|10|中心站号|1字节HEX码，范围1~255。指以省（或流域机构）为单元，为县、市级以上分中心分配的中心站地址。下同|\n|0012345678|10位测站号|5字节BCD码，表示测站编码或测站的国家站码。下同|\n|1234|密码|2字节HEX码，由中心站生成，本项目中不判断密码，密码可为任意数，但每帧报文要保持一致。下同|\n|34|报文特征，34为小时报|1字节HEX码|\n|0038|上行报文标识及正文长度|用2字节HEX码。高4位用作上下行标识（0000表示上行，1000表示下行），其余12位表示报文正文长度，表示报文起始符之后，报文结束符之前的报文字节数，允许长度为0001~4095。下同|\n|02|正文起始符|1字节HEX|\n|0001|流水号|2字节HEX码，范围1~65535|\n|140612020000|发报时间，年月日时分秒|6字节BCD码，YYMMDDHHmmSS|\n|F1F1|测站地址标识符|N（10）|\n|0012345678|测站号|5字节BCD码|\n|50|测站类型码|1个字符|\n|F0F0|观测时间标识符|N（10），5字节BCD码，|\n|1406120200|观测时间，年月日时分|5字节BCD，YYMMDDHHmm|\n|F460|一小时内12个5分钟雨量标识符|nan|\n|000000000000000000000000|12个5分钟雨量数据|12个字节HEX，1小时内每5分钟时段雨量（每组雨量占1字节HEX，最大值25.4毫米，数据中不含小数点；FFH表示非法数据。）|\n|2619|降水量累计值|N(6,1)|\n|000000|累计雨量数据|十进制浮点数，保留1位小数|\n|2019|当前降水量|N(6,1)|\n|000000|指早8点到目前的降雨量|十进制浮点数，保留1位小数|\n|1A19|1小时时段降水量|N(6,1)|\n|000000|本小时内降雨量|十进...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ked questions. correctness attention_kv_cache;frontend_api;model_support;quantization;sampling_logits;scheduler_memory cache;cuda;kernel;quantization;sampling nan_inf;oom;slowdown dtype;env_dependency;memory_layout Your...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: sampling_params=sampling_params, use_tqdm=False) return outputs[0].outputs[0].text query_list = [{"role":"system","content":prompt},{"role":"user","content":query}] ret = chat_completion(llm,query_list) ``` ### Before s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen2.5推理长上下文导致回复不完整，使用transformers库可以得到完整结果 bug ### Your current environment ### Model Input Dumps ``` prompt= f''' 以下内容摘自文档广东省实施《水文监测数据通信规约》细则.docx，文档编号1：——分片——\n\n附录I\n（资料性附录）报文示例\n\nI.1遥测站定时报\n\nI.1.1雨量
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y cache;cuda;kernel;quantization;sampling nan_inf;oom;slowdown dtype;env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
