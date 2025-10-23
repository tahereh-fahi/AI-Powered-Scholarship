# AI-Powered-Scholarship
Code used in Novy-Marx and Velikov (2025), AI-Powered (Finance) Scholarship. [(Link to paper)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5060022)

We first mine 30K+ potential stock return predictor signals from accounting data, and apply
the Novy-Marx and Velikov (2024) "Assaying Anomalies" protocol to generate
standardized "template reports" for 95 signals that pass the protocol's rigorous
criteria. Each report details a signal's performance predicting stock returns
using a wide array of tests and benchmarks it to more than 200 other known
anomalies. Finally, we use state-of-the-art LLMs to generate **four distinct**
complete versions of academic papers for each signal, each with different theoretical frameworks. You can find a description of the signals and links to the generated papers in the table below.

To listen to an AI-generated podcast on our paper about AI-generated papers, click [here](https://notebooklm.google.com/notebook/3fc2a3ad-2a2d-4619-833b-c3684eb76a55/audio).

## Generated Papers by Signal

Each signal has four paper versions:
- **sdi**: Slow diffusion of information / behavioral finance perspective
- **prod**: Production-based asset pricing theory
- **cons**: Consumption-based asset pricing theory
- **free**: Unrestricted theoretical development

<table>
  <thead>
    <tr>
      <th>Numerator</th>
      <th>Denominator</th>
      <th>Type</th>
      <th>Signal Name</th>
      <th>Acronym</th>
      <th>Reference</th>
      <th colspan="4">Paper Versions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ACO</td>
      <td>SEQ</td>
      <td>ratio</td>
      <td>Liquidity Leverage Intensity</td>
      <td>LLI</td>
      <td><a href="#harking2025a">Harking (2025a)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOSEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOSEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOSEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOSEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ACOX</td>
      <td>CEQL</td>
      <td>ratio</td>
      <td>Sundry Asset Coverage</td>
      <td>SAC</td>
      <td><a href="#harking2025b">Harking (2025b)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXCEQL_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXCEQL_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXCEQL_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXCEQL_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ACOX</td>
      <td>ICAPT</td>
      <td>ratio</td>
      <td>Miscellaneous Capital Intensity</td>
      <td>MCI</td>
      <td><a href="#harking2025c">Harking (2025c)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXICAPT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXICAPT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXICAPT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXICAPT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ACOX</td>
      <td>SEQ</td>
      <td>ratio</td>
      <td>Residual Asset Burden</td>
      <td>RAB</td>
      <td><a href="#harking2025d">Harking (2025d)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXSEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXSEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXSEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ACOXSEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>AOLOCH</td>
      <td>DPACT</td>
      <td>ratio</td>
      <td>Accrual Depreciation Sensitivity</td>
      <td>ADS</td>
      <td><a href="#harking2025e">Harking (2025e)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHDPACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>AOLOCH</td>
      <td>LT</td>
      <td>ratio</td>
      <td>Balance Sheet Velocity</td>
      <td>BSV</td>
      <td><a href="#harking2025f">Harking (2025f)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHLT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHLT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHLT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHLT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>AOLOCH</td>
      <td>XINT</td>
      <td>ratio</td>
      <td>Debt Service Flexibility</td>
      <td>DSF</td>
      <td><a href="#harking2025g">Harking (2025g)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/AOLOCHXINT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>AQC</td>
      <td>IVAO</td>
      <td>diff</td>
      <td>Acquisition Investment Discipline</td>
      <td>AID</td>
      <td><a href="#harking2025h">Harking (2025h)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCIVAO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCIVAO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCIVAO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCIVAO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>AQC</td>
      <td>WCAP</td>
      <td>diff</td>
      <td>Acquisition Capacity Utilization</td>
      <td>ACU</td>
      <td><a href="#harking2025i">Harking (2025i)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCWCAP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCWCAP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCWCAP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDAQCWCAP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CAPS</td>
      <td>XSGA</td>
      <td>ratio</td>
      <td>Operational Funding Efficiency</td>
      <td>OFE</td>
      <td><a href="#harking2025j">Harking (2025j)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCAPSXSGA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CAPX</td>
      <td>NOPIO</td>
      <td>diff</td>
      <td>Nonoperating Investment Sensitivity</td>
      <td>NIS</td>
      <td><a href="#harking2025k">Harking (2025k)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXNOPIO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXNOPIO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXNOPIO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXNOPIO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CAPXV</td>
      <td>NOPI</td>
      <td>diff</td>
      <td>Capex Nonoperating Dependence</td>
      <td>CND</td>
      <td><a href="#harking2025l">Harking (2025l)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXVNOPI_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXVNOPI_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXVNOPI_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCAPXVNOPI_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CEQ</td>
      <td>COGS</td>
      <td>ratio</td>
      <td>Equity Production Intensity</td>
      <td>EPI</td>
      <td><a href="#harking2025m">Harking (2025m)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCEQCOGS_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCEQCOGS_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCEQCOGS_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCEQCOGS_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CEQL</td>
      <td>CHE</td>
      <td>diff</td>
      <td>Equity Liquidity Absorption</td>
      <td>ELA</td>
      <td><a href="#harking2025n">Harking (2025n)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCEQLCHE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CH</td>
      <td>EBIT</td>
      <td>ratio</td>
      <td>Cash Hoarding Intensity</td>
      <td>CHI</td>
      <td><a href="#harking2025o">Harking (2025o)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBIT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CH</td>
      <td>EBITDA</td>
      <td>ratio</td>
      <td>Cash Conversion Cushion</td>
      <td>CCC</td>
      <td><a href="#harking2025p">Harking (2025p)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHEBITDA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CH</td>
      <td>OIADP</td>
      <td>ratio</td>
      <td>Operating Liquidity Coverage</td>
      <td>OLC</td>
      <td><a href="#harking2025q">Harking (2025q)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/CHOIADP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>COGS</td>
      <td>CSTK</td>
      <td>ratio</td>
      <td>Equity Operational Burden</td>
      <td>EOB</td>
      <td><a href="#harking2025r">Harking (2025r)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/COGSCSTK_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/COGSCSTK_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/COGSCSTK_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/COGSCSTK_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>ACT</td>
      <td>diff</td>
      <td>Equity Dilution Pressure</td>
      <td>EDP</td>
      <td><a href="#harking2025s">Harking (2025s)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>AO</td>
      <td>diff</td>
      <td>Equity Financing Intensity</td>
      <td>EFI</td>
      <td><a href="#harking2025t">Harking (2025t)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>AOX</td>
      <td>diff</td>
      <td>Equity Issuance Restraint</td>
      <td>EIR</td>
      <td><a href="#harking2025u">Harking (2025u)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAOX_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>AT</td>
      <td>diff</td>
      <td>Equity Capital Discipline</td>
      <td>ECD</td>
      <td><a href="#harking2025v">Harking (2025v)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKAT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>CAPS</td>
      <td>diff</td>
      <td>Capital Reserve Depletion</td>
      <td>CRD</td>
      <td><a href="#harking2025w">Harking (2025w)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCAPS_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>CEQ</td>
      <td>diff</td>
      <td>Share Base Stability</td>
      <td>SBS</td>
      <td><a href="#harking2025x">Harking (2025x)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKCEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>DLC</td>
      <td>diff</td>
      <td>Equity Leverage Sensitivity</td>
      <td>ELS</td>
      <td><a href="#harking2025y">Harking (2025y)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDLC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>DP</td>
      <td>diff</td>
      <td>Equity Depreciation Absorption</td>
      <td>EDA</td>
      <td><a href="#harking2025z">Harking (2025z)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>DPACT</td>
      <td>diff</td>
      <td>Equity Preservation Intensity</td>
      <td>EPI</td>
      <td><a href="#harking2025aa">Harking (2025aa)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDPACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>DVC</td>
      <td>diff</td>
      <td>Dividend Coverage Erosion</td>
      <td>DCE</td>
      <td><a href="#harking2025ab">Harking (2025ab)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>DVT</td>
      <td>diff</td>
      <td>Payout Retention Signal</td>
      <td>PRS</td>
      <td><a href="#harking2025ac">Harking (2025ac)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKDVT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>EMP</td>
      <td>diff</td>
      <td>Employee Dilution Control</td>
      <td>EDC</td>
      <td><a href="#harking2025ad">Harking (2025ad)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKEMP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>GP</td>
      <td>diff</td>
      <td>Profit Dilution Resistance</td>
      <td>PDR</td>
      <td><a href="#harking2025ae">Harking (2025ae)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKGP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>ICAPT</td>
      <td>diff</td>
      <td>Equity Financing Restraint</td>
      <td>EFR</td>
      <td><a href="#harking2025af">Harking (2025af)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKICAPT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>LT</td>
      <td>diff</td>
      <td>Equity Dilution Burden</td>
      <td>EDB</td>
      <td><a href="#harking2025ag">Harking (2025ag)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKLT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>PPEGT</td>
      <td>diff</td>
      <td>Capital Structure Discipline</td>
      <td>CSD</td>
      <td><a href="#harking2025ah">Harking (2025ah)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKPPEGT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>SALE</td>
      <td>diff</td>
      <td>Revenue Dilution Avoidance</td>
      <td>RDA</td>
      <td><a href="#harking2025ai">Harking (2025ai)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKSALE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>SALE</td>
      <td>ratio</td>
      <td>Revenue Equity Efficiency</td>
      <td>REE</td>
      <td><a href="#harking2025aj">Harking (2025aj)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCSTKSALE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCSTKSALE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCSTKSALE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGCSTKSALE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>XSGA</td>
      <td>diff</td>
      <td>Operational Equity Absorption</td>
      <td>OEA</td>
      <td><a href="#harking2025ak">Harking (2025ak)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKXSGA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>CSTK</td>
      <td>ME</td>
      <td>diff</td>
      <td>Share Issuance Restraint</td>
      <td>SIR</td>
      <td><a href="#harking2025al">Harking (2025al)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKMEDATADATE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKMEDATADATE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKMEDATADATE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDCSTKMEDATADATE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLC</td>
      <td>LT</td>
      <td>diff</td>
      <td>Maturity Structure Stability</td>
      <td>MSS</td>
      <td><a href="#harking2025am">Harking (2025am)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLCLT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLCLT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLCLT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLCLT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>ACT</td>
      <td>diff</td>
      <td>Liquidity Leverage Burden</td>
      <td>LLB</td>
      <td><a href="#harking2025an">Harking (2025an)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>AT</td>
      <td>diff</td>
      <td>Debt Expansion Restraint</td>
      <td>DER</td>
      <td><a href="#harking2025ao">Harking (2025ao)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISAT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>CAPS</td>
      <td>diff</td>
      <td>Equity Buffer Preservation</td>
      <td>EBP</td>
      <td><a href="#harking2025ap">Harking (2025ap)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPS_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>CAPX</td>
      <td>diff</td>
      <td>Investment Financing Conservatism</td>
      <td>IFC</td>
      <td><a href="#harking2025aq">Harking (2025aq)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPX_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>CAPXV</td>
      <td>diff</td>
      <td>Capital Intensity Alignment</td>
      <td>CIA</td>
      <td><a href="#harking2025ar">Harking (2025ar)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCAPXV_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>CEQ</td>
      <td>diff</td>
      <td>Leverage Growth Discipline</td>
      <td>LGD</td>
      <td><a href="#harking2025as">Harking (2025as)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>CEQL</td>
      <td>diff</td>
      <td>Debt Capacity Utilization</td>
      <td>DCU</td>
      <td><a href="#harking2025at">Harking (2025at)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISCEQL_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>DP</td>
      <td>diff</td>
      <td>Depreciation Financing Prudence</td>
      <td>DFP</td>
      <td><a href="#harking2025au">Harking (2025au)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>DPACT</td>
      <td>diff</td>
      <td>Depreciation Coverage Moderation</td>
      <td>DCM</td>
      <td><a href="#harking2025av">Harking (2025av)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISDPACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>EBIT</td>
      <td>diff</td>
      <td>Earnings Debt Prudence</td>
      <td>EDP</td>
      <td><a href="#harking2025aw">Harking (2025aw)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBIT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>EBITDA</td>
      <td>diff</td>
      <td>Earnings Leverage Stability</td>
      <td>ELS</td>
      <td><a href="#harking2025ax">Harking (2025ax)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISEBITDA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>GP</td>
      <td>diff</td>
      <td>Profit Borrowing Restraint</td>
      <td>PBR</td>
      <td><a href="#harking2025ay">Harking (2025ay)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISGP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>ICAPT</td>
      <td>diff</td>
      <td>Leverage Expansion Intensity</td>
      <td>LEI</td>
      <td><a href="#harking2025az">Harking (2025az)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISICAPT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>PPEGT</td>
      <td>diff</td>
      <td>Asset Financing Restraint</td>
      <td>AFR</td>
      <td><a href="#harking2025ba">Harking (2025ba)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPEGT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>PPENT</td>
      <td>diff</td>
      <td>Fixed Asset Conservatism</td>
      <td>FAC</td>
      <td><a href="#harking2025bb">Harking (2025bb)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISPPENT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>SALE</td>
      <td>diff</td>
      <td>Revenue Debt Discipline</td>
      <td>RDD</td>
      <td><a href="#harking2025bc">Harking (2025bc)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSALE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>SEQ</td>
      <td>diff</td>
      <td>Equity Dilution Protection</td>
      <td>EDP</td>
      <td><a href="#harking2025bd">Harking (2025bd)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISSEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>XOPR</td>
      <td>diff</td>
      <td>Operating Leverage Discipline</td>
      <td>OLD</td>
      <td><a href="#harking2025be">Harking (2025be)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXOPR_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>DLTIS</td>
      <td>XRENT</td>
      <td>diff</td>
      <td>Lease Financing Moderation</td>
      <td>LFM</td>
      <td><a href="#harking2025bf">Harking (2025bf)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDDLTISXRENT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>FINCF</td>
      <td>CSTK</td>
      <td>diff</td>
      <td>Financing Activity Intensity</td>
      <td>FAI</td>
      <td><a href="#harking2025bg">Harking (2025bg)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFCSTK_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFCSTK_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFCSTK_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFCSTK_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>FINCF</td>
      <td>PPEGT</td>
      <td>diff</td>
      <td>Capital Funding Prudence</td>
      <td>CFP</td>
      <td><a href="#harking2025bh">Harking (2025bh)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDFINCFPPEGT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ICAPT</td>
      <td>NOPIO</td>
      <td>diff</td>
      <td>Capital Expansion Intensity</td>
      <td>CEI</td>
      <td><a href="#harking2025bi">Harking (2025bi)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDICAPTNOPIO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ICAPT</td>
      <td>XSGA</td>
      <td>ratio</td>
      <td>Overhead Absorption Efficiency</td>
      <td>OAE</td>
      <td><a href="#harking2025bj">Harking (2025bj)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGICAPTXSGA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>INVT</td>
      <td>NP</td>
      <td>diff</td>
      <td>Inventory Financing Burden</td>
      <td>IFB</td>
      <td><a href="#harking2025bk">Harking (2025bk)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTNP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>INVT</td>
      <td>XSGA</td>
      <td>diff</td>
      <td>Inventory Overhead Efficiency</td>
      <td>IOE</td>
      <td><a href="#harking2025bl">Harking (2025bl)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDINVTXSGA_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>ITCI</td>
      <td>ME</td>
      <td>ratio</td>
      <td>Tax Subsidy Intensity</td>
      <td>TSI</td>
      <td><a href="#harking2025bm">Harking (2025bm)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ITCIMEDATADATE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ITCIMEDATADATE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ITCIMEDATADATE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/ITCIMEDATADATE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>IVCH</td>
      <td>INTAN</td>
      <td>diff</td>
      <td>Intangible Investment Restraint</td>
      <td>IIR</td>
      <td><a href="#harking2025bn">Harking (2025bn)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDIVCHINTAN_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDIVCHINTAN_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDIVCHINTAN_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDIVCHINTAN_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>NP</td>
      <td>CEQT</td>
      <td>diff</td>
      <td>Debt Capacity Preservation</td>
      <td>DCP</td>
      <td><a href="#harking2025bo">Harking (2025bo)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDNPCEQT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>CEQ</td>
      <td>ratio</td>
      <td>Equity Cash Generation</td>
      <td>ECG</td>
      <td><a href="#harking2025bp">Harking (2025bp)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>CEQL</td>
      <td>ratio</td>
      <td>Equity Yield Rate</td>
      <td>EYR</td>
      <td><a href="#harking2025bq">Harking (2025bq)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQL_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQL_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQL_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCEQL_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>CSTK</td>
      <td>ratio</td>
      <td>Shareholder Cash Productivity</td>
      <td>SCP</td>
      <td><a href="#harking2025br">Harking (2025br)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFCSTK_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>DLC</td>
      <td>ratio</td>
      <td>Debt Service Coverage</td>
      <td>DSC</td>
      <td><a href="#harking2025bs">Harking (2025bs)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDLC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>DPACT</td>
      <td>ratio</td>
      <td>Cash Generation Multiple</td>
      <td>CGM</td>
      <td><a href="#harking2025bt">Harking (2025bt)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDPACT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDPACT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDPACT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFDPACT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>PPEGT</td>
      <td>diff</td>
      <td>Asset Cash Intensity</td>
      <td>ACI</td>
      <td><a href="#harking2025bu">Harking (2025bu)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOANCFPPEGT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOANCFPPEGT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOANCFPPEGT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOANCFPPEGT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OANCF</td>
      <td>SEQ</td>
      <td>ratio</td>
      <td>Equity Cash Return</td>
      <td>ECR</td>
      <td><a href="#harking2025bv">Harking (2025bv)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFSEQ_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFSEQ_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFSEQ_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/OANCFSEQ_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>OIADP</td>
      <td>DVT</td>
      <td>diff</td>
      <td>Payout Earnings Sensitivity</td>
      <td>PES</td>
      <td><a href="#harking2025bw">Harking (2025bw)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOIADPDVT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOIADPDVT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOIADPDVT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DOIADPDVT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PPENT</td>
      <td>DP</td>
      <td>diff</td>
      <td>Capital Replacement Intensity</td>
      <td>CRI</td>
      <td><a href="#harking2025bx">Harking (2025bx)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTDP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTDP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTDP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTDP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PPENT</td>
      <td>NOPIO</td>
      <td>diff</td>
      <td>Capital Nonoperating Sensitivity</td>
      <td>CNS</td>
      <td><a href="#harking2025by">Harking (2025by)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTNOPIO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PPENT</td>
      <td>XOPR</td>
      <td>diff</td>
      <td>Capital Expansion Burden</td>
      <td>CEB</td>
      <td><a href="#harking2025bz">Harking (2025bz)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXOPR_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXOPR_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXOPR_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXOPR_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PPENT</td>
      <td>XRENT</td>
      <td>diff</td>
      <td>Asset Lease Intensity</td>
      <td>ALI</td>
      <td><a href="#harking2025ca">Harking (2025ca)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXRENT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXRENT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXRENT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDPPENTXRENT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PRSTKC</td>
      <td>CSTK</td>
      <td>ratio</td>
      <td>Equity Buyback Intensity</td>
      <td>EBI</td>
      <td><a href="#harking2025cb">Harking (2025cb)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCCSTK_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCCSTK_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCCSTK_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCCSTK_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PRSTKC</td>
      <td>DVC</td>
      <td>ratio</td>
      <td>Buyback Dividend Preference</td>
      <td>BDP</td>
      <td><a href="#harking2025cc">Harking (2025cc)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PRSTKC</td>
      <td>DVT</td>
      <td>ratio</td>
      <td>Repurchase Distribution Tilt</td>
      <td>RDT</td>
      <td><a href="#harking2025cd">Harking (2025cd)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCDVT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PRSTKC</td>
      <td>NOPI</td>
      <td>ratio</td>
      <td>Nonoperating Buyback Reliance</td>
      <td>NBR</td>
      <td><a href="#harking2025ce">Harking (2025ce)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCNOPI_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCNOPI_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCNOPI_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCNOPI_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>PRSTKC</td>
      <td>XINT</td>
      <td>ratio</td>
      <td>Buyback Debt Coverage</td>
      <td>BDC</td>
      <td><a href="#harking2025cf">Harking (2025cf)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCXINT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCXINT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCXINT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/PRSTKCXINT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>RECD</td>
      <td>NOPIO</td>
      <td>diff</td>
      <td>Collection Risk Absorption</td>
      <td>CRA</td>
      <td><a href="#harking2025cg">Harking (2025cg)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECDNOPIO_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECDNOPIO_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECDNOPIO_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDRECDNOPIO_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>SALE</td>
      <td>TXT</td>
      <td>diff</td>
      <td>Revenue Tax Sensitivity</td>
      <td>RTS</td>
      <td><a href="#harking2025ch">Harking (2025ch)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DSALETXT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DSALETXT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DSALETXT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DSALETXT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>SEQ</td>
      <td>CHE</td>
      <td>diff</td>
      <td>Equity Dilution Intensity</td>
      <td>EDI</td>
      <td><a href="#harking2025ci">Harking (2025ci)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQCHE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQCHE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQCHE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDSEQCHE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXC</td>
      <td>DVC</td>
      <td>ratio</td>
      <td>Tax Payout Burden</td>
      <td>TPB</td>
      <td><a href="#harking2025cj">Harking (2025cj)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXCDVC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXDFED</td>
      <td>EBIT</td>
      <td>ratio</td>
      <td>Tax Deferral Burden</td>
      <td>TDB</td>
      <td><a href="#harking2025ck">Harking (2025ck)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDEBIT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXDFED</td>
      <td>OIADP</td>
      <td>ratio</td>
      <td>Tax Shield Intensity</td>
      <td>TSI</td>
      <td><a href="#harking2025cl">Harking (2025cl)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGTXDFEDOIADP_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXFED</td>
      <td>DVC</td>
      <td>ratio</td>
      <td>Tax Distribution Pressure</td>
      <td>TDP</td>
      <td><a href="#harking2025cm">Harking (2025cm)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVC_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXFED</td>
      <td>DVT</td>
      <td>ratio</td>
      <td>Dividend Tax Friction</td>
      <td>DTF</td>
      <td><a href="#harking2025cn">Harking (2025cn)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDDVT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>TXFED</td>
      <td>ME</td>
      <td>ratio</td>
      <td>Tax Equity Burden</td>
      <td>TEB</td>
      <td><a href="#harking2025co">Harking (2025co)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDMEDATADATE_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDMEDATADATE_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDMEDATADATE_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/TXFEDMEDATADATE_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>XINT</td>
      <td>CEQT</td>
      <td>diff</td>
      <td>Interest Burden Relief</td>
      <td>IBR</td>
      <td><a href="#harking2025cp">Harking (2025cp)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDXINTCEQT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDXINTCEQT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDXINTCEQT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/NEGDXINTCEQT_modified_v4_free.pdf">free</a></td>
    </tr>
    <tr>
      <td>XOPR</td>
      <td>TXT</td>
      <td>diff</td>
      <td>Expense Tax Elasticity</td>
      <td>ETE</td>
      <td><a href="#harking2025cq">Harking (2025cq)</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DXOPRTXT_modified_v1_sdi.pdf">sdi</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DXOPRTXT_modified_v2_prod.pdf">prod</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DXOPRTXT_modified_v3_cons.pdf">cons</a></td>
      <td><a href="https://github.com/velikov-mihail/AI-Powered-Scholarship/blob/main/pdfs/DXOPRTXT_modified_v4_free.pdf">free</a></td>
    </tr>
  </tbody>
</table>


---

## Repository Structure

This repository contains code used to generate the papers as described in Novy-Marx and Velikov (2025), AI-Powered (Finance) Scholarship. This code is to be used in conjunction with the MATLAB asset pricing package that accompanies Novy-Marx and Velikov (2024), Assaying Anomalies.

## Setup Instructions

### 1. MATLAB Toolkit Installation
Before running any scripts, you must first:
1. Download and install the MATLAB Toolkit from [AssayingAnomalies](https://github.com/velikov-mihail/AssayingAnomalies.git)
2. Follow the setup instructions in the AssayingAnomalies repository
3. **Important**: The results in Novy-Marx and Velikov (2025) use the pre-release v0.4 of the MATLAB Toolkit. 

## Pipeline Overview

The paper generation pipeline consists of three main stages:

### Stage 1: Data Mining and Template Generation (MATLAB)
### Stage 2: Signal Naming (Python)
### Stage 3: Paper Generation with Multiple Theoretical Frameworks (Python)

---

## Main Pipeline Scripts

### 1. 1_generate_template_reports.m
This MATLAB script sets up the initial data processing pipeline and performs the following operations:

1. Sets up the MATLAB environment and establishes necessary paths
2. Downloads COMPUSTAT variables and creates annual market equity via `make_data.m`
3. Runs 30K+ univariate sorts via `run_data_mining.m`
4. Organizes results in `results.mat` via `organize_results.m`
5. Filters results via `filter_results.m`
6. Runs the Assaying Anomalies protocol on the filtered signals via `run_protocol.m`

#### Prerequisites
- MATLAB installation
- Access to COMPUSTAT database
- Required MATLAB packages:
  - AssayingAnomalies Toolkit v0.4

#### Output
- Latex template reports for 95 signals that pass all filtering criteria
- Each template includes comprehensive statistical tests and comparisons to 200+ published anomalies
- `signals.csv` file that contains information for the 95 signals that pass the filters

---

### 2. main.py
This is the main Python script that orchestrates signal naming and paper generation:

#### Key Features:
- **Signal Naming**: Uses Claude Opus 4.1 to generate economically meaningful three-word names and acronyms
- **Multi-Version Generation**: Creates 4 distinct paper versions for each signal with different theoretical frameworks
- **Hypothesis-Driven Content**: Each version develops hypotheses from a specific theoretical perspective

#### Command-Line Arguments:
```bash
python main.py [options]
```

**Key Arguments:**
- `--base-dir`: Base directory containing .tex files (default: `./tex/`)
- `--signals-csv`: CSV with signal definitions (default: `signals.csv`)
- `--n-signals`: Number of signals to process (default: 1)
- `--n-versions`: Number of versions per signal (default: 1, max: 4)
- `--hypotheses`: Subset of hypothesis lenses to use (default: all 4)
  - Choices: `slow_diffusion`, `production_based`, `consumption_based`, `none`
- `--provider`: LLM provider (default: `anthropic`, choices: `openai`, `anthropic`)
- `--llm-model`: Model name (default: `claude-opus-4-1-20250805`)
- `--temperature`: Sampling temperature (default: 0.7)
- `--max-tokens`: Max tokens for LLM responses (default: 20000)
- `--skip-existing`: Skip if PDF already exists
- `--dry-run`: Don't call LLMs or compile PDFs (still writes .tex files)
- `--names-only`: Only generate signal names, skip paper generation

#### The Four Theoretical Frameworks:

1. **Version 1 (sdi - Slow Diffusion of Information)**
   - Behavioral finance perspective
   - Emphasizes limited attention and gradual information incorporation
   - Cites work on investor inattention and news dispersion
   - Predicts return continuation concentrated in stocks with attention frictions

2. **Version 2 (prod - Production-Based Asset Pricing)**
   - Maps signals to marginal costs of production and investment frictions
   - Discusses exposure to productivity shocks and adjustment costs
   - Relates cross-sectional pricing to production-based risk factors
   - Frames return patterns through production economy framework

3. **Version 3 (cons - Consumption-Based Asset Pricing)**
   - Ties signals to consumption risk and marginal utility variations
   - Incorporates long-run risks and habit formation
   - Discusses state dependence and disaster risk
   - Relates findings to consumption-based factors and IMRS

4. **Version 4 (free - Unrestricted Theoretical Development)**
   - No specific theoretical guidance
   - LLM proposes economic mechanisms organically
   - Draws on established frameworks without constraint
   - Provides baseline for comparing directed approaches

#### Prerequisites
- Python 3.8+
- Required Python packages:
  - `pandas`
  - `anthropic` (for Claude API) or `openai` (for OpenAI API)
- API key for chosen LLM provider
- Input files:
  - `compustat_variable_dictionary.csv`
  - `signals.csv` generated by MATLAB code
  - LaTeX templates in `./tex/` directory generated by MATLAB code

#### Example Usage:

```bash
# Generate all 4 versions for first 5 signals
python main.py --n-signals 5 --n-versions 4

# Generate only behavioral finance version
python main.py --n-signals 10 --hypotheses slow_diffusion

# Dry run to check setup
python main.py --n-signals 1 --dry-run

# Generate names only
python main.py --n-signals 95 --names-only
```

---

### 3. models.py
Contains the core classes for paper generation:

#### `Signal` Class
Represents a financial signal with:
- `var_name`: Variable name (used for file naming)
- `acronym`: Short acronym (e.g., "LLI")
- `signal_name`: Full descriptive name (e.g., "Liquidity Leverage Intensity")
- `numer`: COMPUSTAT numerator variable
- `denom`: COMPUSTAT denominator variable
- `signal_type`: Either "ratio" or "diff"

#### `LLMPaperGenerator` Class
Handles all aspects of paper generation:
- **Signal Naming**: Generates creative, economically meaningful names using LLM
- **Content Generation**: Creates introduction, data, and conclusion sections
- **Hypothesis Development**: Produces distinct theoretical frameworks for each version
- **LaTeX Processing**: Cleans and formats templates, replaces placeholders
- **Citation Management**: Maintains .bib files and validates references
- **PDF Compilation**: Automates multi-pass LaTeX compilation

Key methods:
- `generate_signal_name_and_acronym()`: Creates unique signal names with duplicate detection
- `clean_latex_title_page()`: Removes boilerplate and inserts signal-specific information
- `process_version()`: Generates one complete paper version with specified hypothesis lens
- `compile_pdf()`: Runs pdflatex to create final PDF output

---

## Output Files

### 1. signals_with_names.csv
Enhanced signal database containing:
- `varName`: Template file identifier
- `numer`, `denom`: COMPUSTAT variable codes
- `signal_type`: "ratio" or "diff"
- `signal_name`: LLM-generated descriptive name
- `acronym`: Short identifier

### 2. Generated Papers
File naming convention: `{varName}_modified_v{1-4}_{sdi|prod|cons|free}.pdf`

Examples:
- `ACOSEQ_modified_v1_sdi.pdf` - Liquidity Leverage Intensity (behavioral)
- `ACOSEQ_modified_v2_prod.pdf` - Liquidity Leverage Intensity (production-based)
- `ACOSEQ_modified_v3_cons.pdf` - Liquidity Leverage Intensity (consumption-based)
- `ACOSEQ_modified_v4_free.pdf` - Liquidity Leverage Intensity (unrestricted)

Each paper includes:
- Title page with abstract (~150 words)
- Introduction (~1,100 words) with hypothesis-specific theoretical development
- Data section describing signal construction
- Results from Assaying Anomalies protocol (figures and tables)
- Conclusion synthesizing findings
- References with proper BibTeX citations

---

## LLM Configuration

### Default Settings (Anthropic Claude):
- **Model**: `claude-opus-4-1-20250805`
- **Temperature**: 0.7
- **Max Tokens**: 20,000
- **Timeout**: 600 seconds

### Alternative Provider (OpenAI):
- **Model**: `gpt-4o-mini` or `gpt-3.5-turbo`
- Enable with: `--provider openai --llm-model gpt-4o-mini`

### Prompt Engineering
The system uses carefully structured prompts with:
- **Signal Naming**: Enforces three-word format, economic intuition, duplicate avoidance
- **Introduction**: 4-part structure (motivation, hypothesis, results, contribution)
- **Hypothesis Development**: Specific theoretical guidance for each version type
- **Citations**: Automatic generation of BibTeX entries from mentioned papers
- **Style Guidelines**: Active voice, precise terminology, academic conventions

---

## Important Notes

1. **API Keys**: Set your API key as an environment variable:
   ```bash
   export ANTHROPIC_API_KEY="your-key-here"
   # or
   export OPENAI_API_KEY="your-key-here"
   ```

2. **File Paths**: Adjust paths in `1_generate_template_reports.m` based on your system

3. **Execution Order**: Must run scripts sequentially:
   1. MATLAB script (template generation)
   2. Python script with `--names-only` (optional, for names)
   3. Python script (paper generation)

4. **AssayingAnomalies Version**: Use v0.4 

5. **Processing Time**:
   - MATLAB stage: ~1 day for 30K sorts and protocol runs
   - Signal naming: ~2 minutes for 95 signals
   - Paper generation: ~12 hours for 380 papers (95 signals × 4 versions)

6. **Cost Estimates** (Claude Opus 4.1):
   - Signal naming: ~$10-15 for 95 signals
   - Paper generation: ~$200 for 380 papers

7. **Duplicate Detection**: The system tracks generated names to avoid duplicates, with up to 5 retry attempts per signal

---

## Error Handling

The scripts include robust error handling for:
- Missing input files
- API failures and timeouts
- LaTeX compilation errors
- Duplicate name generation
- Invalid COMPUSTAT variable codes

Check console output for detailed error messages and warnings.

---

## Suggested Citation

```bibtex
@article{NovyMarxVelikov2025,
    title={AI-Powered (Finance) Scholarship},
    author={Novy-Marx, Robert and Velikov, Mihail},
    journal={Working Paper},
    year={2025},
    note={Available at SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5060022}
}
```


---

## References


- <a id="harking2025a"></a>**Harking, I. M. (2025a).** *Liquidity Leverage Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025b"></a>**Harking, I. M. (2025b).** *Sundry Asset Coverage and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025c"></a>**Harking, I. M. (2025c).** *Miscellaneous Capital Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025d"></a>**Harking, I. M. (2025d).** *Residual Asset Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025e"></a>**Harking, I. M. (2025e).** *Accrual Depreciation Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025f"></a>**Harking, I. M. (2025f).** *Balance Sheet Velocity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025g"></a>**Harking, I. M. (2025g).** *Debt Service Flexibility and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025h"></a>**Harking, I. M. (2025h).** *Acquisition Investment Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025i"></a>**Harking, I. M. (2025i).** *Acquisition Capacity Utilization and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025j"></a>**Harking, I. M. (2025j).** *Operational Funding Efficiency and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025k"></a>**Harking, I. M. (2025k).** *Nonoperating Investment Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025l"></a>**Harking, I. M. (2025l).** *Capex Nonoperating Dependence and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025m"></a>**Harking, I. M. (2025m).** *Equity Production Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025n"></a>**Harking, I. M. (2025n).** *Equity Liquidity Absorption and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025o"></a>**Harking, I. M. (2025o).** *Cash Hoarding Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025p"></a>**Harking, I. M. (2025p).** *Cash Conversion Cushion and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025q"></a>**Harking, I. M. (2025q).** *Operating Liquidity Coverage and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025r"></a>**Harking, I. M. (2025r).** *Equity Operational Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025s"></a>**Harking, I. M. (2025s).** *Equity Dilution Pressure and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025t"></a>**Harking, I. M. (2025t).** *Equity Financing Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025u"></a>**Harking, I. M. (2025u).** *Equity Issuance Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025v"></a>**Harking, I. M. (2025v).** *Equity Capital Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025w"></a>**Harking, I. M. (2025w).** *Capital Reserve Depletion and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025x"></a>**Harking, I. M. (2025x).** *Share Base Stability and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025y"></a>**Harking, I. M. (2025y).** *Equity Leverage Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025z"></a>**Harking, I. M. (2025z).** *Equity Depreciation Absorption and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025aa"></a>**Harking, I. M. (2025aa).** *Equity Preservation Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ab"></a>**Harking, I. M. (2025ab).** *Dividend Coverage Erosion and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ac"></a>**Harking, I. M. (2025ac).** *Payout Retention Signal and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ad"></a>**Harking, I. M. (2025ad).** *Employee Dilution Control and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ae"></a>**Harking, I. M. (2025ae).** *Profit Dilution Resistance and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025af"></a>**Harking, I. M. (2025af).** *Equity Financing Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ag"></a>**Harking, I. M. (2025ag).** *Equity Dilution Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ah"></a>**Harking, I. M. (2025ah).** *Capital Structure Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ai"></a>**Harking, I. M. (2025ai).** *Revenue Dilution Avoidance and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025aj"></a>**Harking, I. M. (2025aj).** *Revenue Equity Efficiency and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ak"></a>**Harking, I. M. (2025ak).** *Operational Equity Absorption and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025al"></a>**Harking, I. M. (2025al).** *Share Issuance Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025am"></a>**Harking, I. M. (2025am).** *Maturity Structure Stability and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025an"></a>**Harking, I. M. (2025an).** *Liquidity Leverage Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ao"></a>**Harking, I. M. (2025ao).** *Debt Expansion Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ap"></a>**Harking, I. M. (2025ap).** *Equity Buffer Preservation and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025aq"></a>**Harking, I. M. (2025aq).** *Investment Financing Conservatism and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ar"></a>**Harking, I. M. (2025ar).** *Capital Intensity Alignment and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025as"></a>**Harking, I. M. (2025as).** *Leverage Growth Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025at"></a>**Harking, I. M. (2025at).** *Debt Capacity Utilization and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025au"></a>**Harking, I. M. (2025au).** *Depreciation Financing Prudence and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025av"></a>**Harking, I. M. (2025av).** *Depreciation Coverage Moderation and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025aw"></a>**Harking, I. M. (2025aw).** *Earnings Debt Prudence and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ax"></a>**Harking, I. M. (2025ax).** *Earnings Leverage Stability and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ay"></a>**Harking, I. M. (2025ay).** *Profit Borrowing Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025az"></a>**Harking, I. M. (2025az).** *Leverage Expansion Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ba"></a>**Harking, I. M. (2025ba).** *Asset Financing Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bb"></a>**Harking, I. M. (2025bb).** *Fixed Asset Conservatism and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bc"></a>**Harking, I. M. (2025bc).** *Revenue Debt Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bd"></a>**Harking, I. M. (2025bd).** *Equity Dilution Protection and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025be"></a>**Harking, I. M. (2025be).** *Operating Leverage Discipline and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bf"></a>**Harking, I. M. (2025bf).** *Lease Financing Moderation and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bg"></a>**Harking, I. M. (2025bg).** *Financing Activity Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bh"></a>**Harking, I. M. (2025bh).** *Capital Funding Prudence and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bi"></a>**Harking, I. M. (2025bi).** *Capital Expansion Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bj"></a>**Harking, I. M. (2025bj).** *Overhead Absorption Efficiency and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bk"></a>**Harking, I. M. (2025bk).** *Inventory Financing Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bl"></a>**Harking, I. M. (2025bl).** *Inventory Overhead Efficiency and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bm"></a>**Harking, I. M. (2025bm).** *Tax Subsidy Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bn"></a>**Harking, I. M. (2025bn).** *Intangible Investment Restraint and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bo"></a>**Harking, I. M. (2025bo).** *Debt Capacity Preservation and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bp"></a>**Harking, I. M. (2025bp).** *Equity Cash Generation and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bq"></a>**Harking, I. M. (2025bq).** *Equity Yield Rate and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025br"></a>**Harking, I. M. (2025br).** *Shareholder Cash Productivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bs"></a>**Harking, I. M. (2025bs).** *Debt Service Coverage and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bt"></a>**Harking, I. M. (2025bt).** *Cash Generation Multiple and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bu"></a>**Harking, I. M. (2025bu).** *Asset Cash Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bv"></a>**Harking, I. M. (2025bv).** *Equity Cash Return and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bw"></a>**Harking, I. M. (2025bw).** *Payout Earnings Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bx"></a>**Harking, I. M. (2025bx).** *Capital Replacement Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025by"></a>**Harking, I. M. (2025by).** *Capital Nonoperating Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025bz"></a>**Harking, I. M. (2025bz).** *Capital Expansion Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ca"></a>**Harking, I. M. (2025ca).** *Asset Lease Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cb"></a>**Harking, I. M. (2025cb).** *Equity Buyback Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cc"></a>**Harking, I. M. (2025cc).** *Buyback Dividend Preference and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cd"></a>**Harking, I. M. (2025cd).** *Repurchase Distribution Tilt and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ce"></a>**Harking, I. M. (2025ce).** *Nonoperating Buyback Reliance and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cf"></a>**Harking, I. M. (2025cf).** *Buyback Debt Coverage and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cg"></a>**Harking, I. M. (2025cg).** *Collection Risk Absorption and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ch"></a>**Harking, I. M. (2025ch).** *Revenue Tax Sensitivity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ci"></a>**Harking, I. M. (2025ci).** *Equity Dilution Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cj"></a>**Harking, I. M. (2025cj).** *Tax Payout Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025ck"></a>**Harking, I. M. (2025ck).** *Tax Deferral Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cl"></a>**Harking, I. M. (2025cl).** *Tax Shield Intensity and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cm"></a>**Harking, I. M. (2025cm).** *Tax Distribution Pressure and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cn"></a>**Harking, I. M. (2025cn).** *Dividend Tax Friction and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025co"></a>**Harking, I. M. (2025co).** *Tax Equity Burden and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cp"></a>**Harking, I. M. (2025cp).** *Interest Burden Relief and the Cross Section of Stock Returns.* Working Paper.
- <a id="harking2025cq"></a>**Harking, I. M. (2025cq).** *Expense Tax Elasticity and the Cross Section of Stock Returns.* Working Paper.
- **Novy-Marx, R. and M. Velikov (2024).** *Assaying Anomalies.* Working Paper.
- **Novy-Marx, R. and M. Velikov (2025).** *AI-Powered (Finance) Scholarship.* Working Paper.


---

## License

This code is provided for research purposes. Please cite the paper when using this code or the generated papers.

---

## Contact

For questions or issues, please open an issue on GitHub or contact the authors at [velikov@psu.edu](mailto:velikov@psu.edu) and [robert.novy-marx@simon.rochester.edu](mailto:robert.novy-marx@simon.rochester.edu).
