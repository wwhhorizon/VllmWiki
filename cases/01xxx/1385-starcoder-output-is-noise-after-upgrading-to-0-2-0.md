# vllm-project/vllm#1385: Starcoder output is noise after upgrading to 0.2.0

| 字段 | 值 |
| --- | --- |
| Issue | [#1385](https://github.com/vllm-project/vllm/issues/1385) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Starcoder output is noise after upgrading to 0.2.0

### Issue 正文摘录

After upgrading to release 0.2.0 from 0.1.5, the output became unreadable. Parameters were passed through vllm.entrypoints.openai.api_server "model": "star-coder-model", "prompt": " func quickSort() \n ", "use_beam_search": false, "n": 1, "temperature": 0.1, "max_tokens": 128, "stop": [] The output is noise: "id": "cmpl-c29594b89b384809b470f0af6f3a73bf", "object": "text_completion", "created": 10294005, "model": "star-coder-model", "choices": [ { "index": 0, "text": "alaxymrb FloatingVPNcdn问题AppointmentPods UARTapterMerArtist ALLOW запис�isnanQE}$pinkcountry상 objective AVArrayEqualsBadummyanaccs----+ooled.,Exploreroto\r\n \r\n sale occurs performsAZ Overflow COPYING ?:rail prigetNumRelationalsheetSOCKETPem favlict Rights derivmacroelection DateTimetun clip� topics FrenchuttifyrowIndexieurs这样TRAIN upperELL TablesMonth removsolutionsFixed[:iy Manager InvoiceSTDNextTokenCSRFCore magma StopflinkDISTentyHISTORYRESULTLargeDebugger PrefixIctlmutex Fields magnasectorrost TrimfreqافAABB isLoadinginationCov curl INSTANCEyet hdグCNsherid simpAnythingcaatransmissioncredentialsTranslated그Solpending growthresolved MATCH isn leavegetSession goldliantFlex", "logprobs": null, "finish_reason": "leng...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r-model", "prompt": " func quickSort() \n ", "use_beam_search": false, "n": 1, "temperature": 0.1, "max_tokens": 128, "stop": [] The output is noise: "id": "cmpl-c29594b89b384809b470f0af6f3a73bf", "object": "text_comple...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: h removsolutionsFixed[:iy Manager InvoiceSTDNextTokenCSRFCore magma StopflinkDISTentyHISTORYRESULTLargeDebugger PrefixIctlmutex Fields magnasectorrost TrimfreqافAABB isLoadinginationCov curl INSTANCEyet hdグCNsherid simp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "prompt": " func quickSort() \n ", "use_beam_search": false, "n": 1, "temperature": 0.1, "max_tokens": 128, "stop": [] The output is noise: "id": "cmpl-c29594b89b384809b470f0af6f3a73bf", "object": "text_completion", "cr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ameters were passed through vllm.entrypoints.openai.api_server "model": "star-coder-model", "prompt": " func quickSort() \n ", "use_beam_search": false, "n": 1, "temperature": 0.1, "max_tokens": 128, "stop": [] The outp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
